# 本体论入门指南

*从文档到知识库的知识工程实践*

这是一份知识工程教程。我们会用本体（Ontology）描述概念和关系，再把文档中的事实和证据整理成可以查询的知识库。我想弄清楚一个查资料时经常遇到的问题：两份文档提到同一个名字，它们说的是同一个对象吗？要回答这个问题，需要逐步明确概念、关系和证据。

第一章从去浙江图书馆借书讲起，沿着同一个问题看 RAG、SAG2 和 GraphRAG 怎样找到材料。后面的章节用作品署名作为练习，逐步学习怎样定义角色、区分版本，并把一条结论追溯到原文。

从[第 0 章 · 课程说明](00-course-overview/0-course-overview.md)开始，再依次阅读 [1.1 借书场景](01-how-existing-systems-organize-knowledge/1-1-borrowing-scenario.md) → [1.2 Agent 怎样查资料、回答借书问题？](01-how-existing-systems-organize-knowledge/1-2-source-materials.md) → [1.3 原始资料怎样整理入库？](01-how-existing-systems-organize-knowledge/1-3-rag-retrieval.md)，或查看[完整逐节教学大纲](tutorial-planning/本体论-逐节教学大纲.md)。动手练习可使用[署名样例数据](examples/media/participations.csv)和[角色查询示例](examples/media/roles.py)。

## 学习路线

| 阶段 | 需要回答的问题 | 对应章节 |
| --- | --- | --- |
| 从现状到问题 | RAG、LLM Wiki 和业务表怎样组织知识？哪些错答值得用本体处理？ | 1–3 |
| 建模与抽取 | 怎样从 CQ 建模并整合旧模型，管理权威记录和术语，把候选事实审核为正式记录？ | 4–7 |
| 查询与验证 | 怎样把 SPARQL 接入现有检索，用 PROV-O 追来源，并定位错答？ | 8–10 |
| 治理与交付 | 怎样维护概念与数据，验收并重建第一版知识库？ | 11–12 |

## 延伸阅读

[教程配图、论文与工程资料](assets/README.md)

[GSA 指南简体中文译本](https://github.com/hansenz42/guides_4_AIagents/tree/206bfbe/translate/zh-CN)中的能力问题设计、从能力问题到本体、BFO 自顶向下建模三篇可配合第一阶段阅读。[本地英文参考材料](references/ontology/gsa-guides/)保留了这三篇指南。

原创教程、代码和教学数据采用 [MIT License](LICENSE)。随仓库收录的 GSA 英文指南沿用[上游许可](references/ontology/gsa-guides/LICENSE.md)，来源为 [GSA 指南仓库](https://github.com/GSA/guides_4_AIagents/tree/5e5ba20b83a52d9b3f4ff00fde19f079483633e1)。
