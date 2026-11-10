# 教程资源

## 教程首页

### 配图

- [知识图谱标志](images/ontology-mark.png) · 用两条共享主语的三元组表示节点之间的关系，用于[教程首页](../README.md)。

## 第 0 章 · 课程说明

[阅读正文](../00-course-overview/0-course-overview.md)

### 配图

- [借阅服务公告](images/library-notice.png) · 为本课生成的模拟公告。
- [从检索到答复的流程](images/borrowing-retrieval-flow.svg) · 从主页补查公告，对照各份原件，标出可以回答和仍待核实的内容。
- [从材料到借书答复](images/borrowing-evidence-graph.svg) · 展示 Agent 查找材料、本体约束下的事实核对，以及证据能支持的结论。

### 原始论文

- [RAG · Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [SAG2 · Embedding-Free Multi-Hop Retrieval with BM25 and JEV](https://arxiv.org/abs/2610.22588)
- [GraphRAG · From Local to Global](https://arxiv.org/abs/2404.16130)

### 工程资料

- [Agent 开发说明](https://www.anthropic.com/engineering/building-effective-agents)
- [长期任务中的 Harness 设计](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

## 第 1 章 · 外部知识的组织与检索方法概览

[阅读 1.1 借书场景](../01-how-existing-systems-organize-knowledge/1-1-borrowing-scenario.md)

### 配图

- [第一次去图书馆](images/first-library-visit.png) · 说明首次借书前还要办理读者证。
- [Agent 怎样回答借书问题](images/agent-library-query.svg) · 对照三个处理步骤，说明模型的常识和馆方资料分别怎样用于这次查询。
- [Agent 处理借书请求的四个步骤](images/agent-request-steps.svg) · 配合[第 1.2 节](../01-how-existing-systems-organize-knowledge/1-2-source-materials.md)梳理从收到提问到给出答复的过程。
- [馆方原件与周日闭馆时间](images/library-source-guide.svg) · 配合[第 1.2 节](../01-how-existing-systems-organize-knowledge/1-2-source-materials.md)对照四份模拟原件，并展开时间表 B。
- [从馆方原件到可检索的片段](images/document-preprocessing.svg) · 配合[第 1.3 节](../01-how-existing-systems-organize-knowledge/1-3-rag-retrieval.md)说明资料预处理的五个步骤。

### 工程资料

- [片段上下文的工程实验](https://www.anthropic.com/research/contextual-retrieval) · 对照[第 1.3 节](../01-how-existing-systems-organize-knowledge/1-3-rag-retrieval.md)的分片示例，了解片段脱离原文后可能丢失哪些信息。
