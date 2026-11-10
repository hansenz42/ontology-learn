<img src="assets/images/ontology-mark.png" width="112" alt="教程标志：两条有向关系从同一节点分别指向两个对象">

# 本体论入门指南

*从文档到知识库的知识工程实践*

本教程介绍如何将文档中的事实、关系和证据组织成可查询、可验证、可维护的知识库。课程以图书馆资料为例，介绍检索增强生成（RAG）的文档处理、证据检索与答案评估，并讨论哪些查询需求值得引入本体建模。

建模从**能力问题**（Competency Question，CQ）开始，即明确知识库需要回答哪些问题。问题决定了模型需要区分哪些概念、描述哪些关系，也为查询结果提供了验收标准。课程随后介绍如何依据本体解析文档、抽取和审核事实，用 RDF 三元组表达事实及其关系，构成知识图谱。图谱通过 SPARQL 提供查询，每条结论都可追溯到支持它的原文。

**面向人群**包括计算机工程专业学生、为企业建设知识库的软件工程师和程序员，以及负责检索与知识系统设计的架构师。

## 章节内容

第 0 章和第 1 章已提供正文，第 2–12 章为课程规划。

| 章节 | 主要内容 |
| --- | --- |
| [第 0 章 · 课程说明](00-course-overview/0-course-overview.md) | 知识工程的目标，本体在知识库中的作用，三元组的基本结构，以及建模的收益与维护成本。 |
| [第 1 章 · 外部知识的组织与检索方法概览](01-how-existing-systems-organize-knowledge/1-1-borrowing-scenario.md) | Agent 如何获取外部资料。比较基础 RAG 的召回与重排、SAG2 的多轮检索和 GraphRAG 的跨文档检索，介绍答案生成与证据核对方法。 |
| 第 2 章 · 从检索到作答的常见错误与成因 | 资料缺失、检索遗漏、记录过时和引用不足如何影响答案，以及如何定位错误最早出现的环节。 |
| 第 3 章 · 知识工程导论 | 对象身份的判定、领域本体中的概念与关系，以及如何根据查询需求和维护成本确定建模范围。 |
| 第 4 章 · 能力问题 | 从业务需求提炼能力问题，用正例、反例和证据不足的情况界定预期答案，形成验收标准。 |
| 第 5 章 · 本体建模与模型整合 | 从能力问题确定类、标识、关系和约束，用 RDF 表达模型实例，并处理已有模型的复用、映射与定义冲突。 |
| 第 6 章 · 权威记录与受控词表 | 各类事实的权威来源与维护责任，使用 SKOS 管理概念、首选名称和别名，以及跨部门词表的对齐。 |
| 第 7 章 · 依据本体处理文档 | 文档解析、表格映射、候选事实抽取、实体消歧与去重，以及保留证据位置和审核决定的方法。 |
| 第 8 章 · 知识图谱查询 | 用 SPARQL 匹配图中的关系、回答能力问题，并将查询结果及证据接入已有检索流程。 |
| 第 9 章 · 来源追溯与更正 | 用 PROV-O 描述原始资料、处理活动与知识记录之间的关系，追踪更正过程并查询历史记录。 |
| 第 10 章 · 验证、测试与调试 | 数据约束检查、能力问题的回归测试，以及模型、数据和查询程序中的错误定位。 |
| 第 11 章 · 数据流与变更治理 | 从原始资料到知识库和检索索引的数据流，本体与事实的变更管理，以及更正或撤回资料后的影响分析。 |
| 第 12 章 · 知识库交付与验收 | 第一版知识库的交付内容、使用独立材料验证查询结果与出处的方法，以及知识库重建。 |

## 总体参考资料

[1] LEWIS P, PEREZ E, PIKTUS A, et al. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)[C/OL]. Advances in Neural Information Processing Systems, 2020, 33: 9459–9474[2026-11-10].

[2] WU Y. [SAG2: Embedding-Free Multi-Hop Retrieval with BM25 and JEV](https://arxiv.org/abs/2610.22588)[PP/OL]. arXiv:2610.22588, 2026[2026-11-10].

[3] EDGE D, TRINH H, CHENG N, et al. [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130)[PP/OL]. arXiv:2404.16130, 2024（2025-02-19 修订）[2026-11-10].

[4] KEET C M. [An Introduction to Ontology Engineering](https://people.cs.uct.ac.za/~mkeet/files/OEbook.pdf)[M/OL]. Version 1.5, 2020[2026-11-10].

[5] HOGAN A, BLOMQVIST E, COCHEZ M, et al. [Knowledge Graphs](https://kgbook.org/)[M/OL]. Springer, 2021[2026-11-10].

[6] U.S. GENERAL SERVICES ADMINISTRATION. [guides_4_AIagents](https://github.com/GSA/guides_4_AIagents)[EB/OL]. GitHub[2026-11-10].

[7] ONTOLOGY ENGINEERING GROUP. [LOT-resources](https://github.com/oeg-upm/LOT-resources)[EB/OL]. GitHub[2026-11-10].

[8] WORLD WIDE WEB CONSORTIUM. [RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/)[EB/OL]. W3C Working Group Note, 2014-06-24[2026-11-10].

[9] WORLD WIDE WEB CONSORTIUM. [OWL 2 Web Ontology Language Primer (Second Edition)](https://www.w3.org/TR/owl2-primer/)[S/OL]. W3C Recommendation, 2012-12-11[2026-11-10].

[10] WORLD WIDE WEB CONSORTIUM. [SKOS Simple Knowledge Organization System Primer](https://www.w3.org/TR/skos-primer/)[EB/OL]. W3C Working Group Note, 2009-08-18[2026-11-10].

[11] WORLD WIDE WEB CONSORTIUM. [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/)[S/OL]. W3C Recommendation, 2013-03-21[2026-11-10].

[12] WORLD WIDE WEB CONSORTIUM. [PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/)[S/OL]. W3C Recommendation, 2013-04-30[2026-11-10].

[13] WORLD WIDE WEB CONSORTIUM. [Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/)[S/OL]. W3C Recommendation, 2017-07-20[2026-11-10].

[14] ANTHROPIC. [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)[EB/OL]. 2024-12-19[2026-11-10].

[15] ANTHROPIC. [Introducing Contextual Retrieval](https://www.anthropic.com/research/contextual-retrieval)[EB/OL]. 2024-09-19[2026-11-10].

[16] MICROSOFT. [Improve RAG chain quality](https://learn.microsoft.com/en-us/azure/databricks/agents/tutorials/ai-cookbook/quality-rag-chain)[EB/OL]. Microsoft Learn[2026-11-10].

[17] RDFLib. [RDFLib](https://github.com/RDFLib/rdflib)[CP/OL]. GitHub[2026-11-10].

[18] RDFLib. [pySHACL](https://github.com/RDFLib/pySHACL)[CP/OL]. GitHub[2026-11-10].

GSA 指南另有[简体中文译本](https://github.com/hansenz42/guides_4_AIagents/tree/206bfbe/translate/zh-CN)，仓库收录了其中三篇指南的[英文原文](references/ontology/gsa-guides/)。

正文引用的论文、工程资料，以及为课程编写的模拟公告和配图，按章节收录在[教程资源索引](assets/README.md)。全课程的参考书目和工具清单见[教学大纲与资料清单](tutorial-planning/本体驱动的知识工程开源教程-教学大纲与资料清单.md)。

## 许可协议（License）

原创教程、示例代码和教学数据采用 **MIT License**。复制或分发这些内容时，请按许可条款保留版权声明和许可声明。[MIT 许可全文](LICENSE)

仓库收录的 GSA 英文指南沿用上游的 **CC0 1.0** 声明。[GSA 许可说明](references/ontology/gsa-guides/LICENSE.md) · [上游仓库](https://github.com/GSA/guides_4_AIagents/tree/5e5ba20b83a52d9b3f4ff00fde19f079483633e1)
