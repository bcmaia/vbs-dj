import cohere


class ApiMaster:
    def __init__(self, token: str, active: bool) -> None:
        self.__token = token
        self.__active = active

    def connect(self):
        if not self.__active: return self
        self.__co = cohere.Client(self.__token)
        return self

    def embed(self, txt):
        if not self.__active: return None
        txt = [str(x) for x in txt] if isinstance(txt, list) else [str(txt)]
        return self.__co.embed(
            texts=txt,
            model="small",
        ).embeddings

    def rerank(self, query, docs, top_n):
        if not self.__active: return None
        if not isinstance(docs, list): docs = [docs]

        return self.__co.rerank(
            model='rerank-english-v2.0',
            query=query,
            documents=docs,
            top_n=top_n
        ).results