---
name: unknown_workflow_vae_5
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.857
common_nodes: [EmptyLatentImage, RH_LLMAPI_NODE, SaveImage, ShellAgentPluginOutputText, Text Multiline, VAEDecode, easy showAnything]
problems: []
missing: []
members: [平台全量/剧本到分镜_2000810138401468418.json, 平台全量/剧本到分镜_2013911790375145473.json, 平台全量/场景设计(文）_2001252110551445505.json, 平台全量/小说到剧本_2000813261236957186.json, 平台全量/角色设计词_2001210035856343041.json, 平台全量/道具设计(文)_2001254963479183361.json]
source: knowledge_consolidation
---

# unknown_workflow_vae_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/剧本到分镜_2000810138401468418.json、平台全量/剧本到分镜_2013911790375145473.json、平台全量/场景设计(文）_2001252110551445505.json、平台全量/小说到剧本_2000813261236957186.json、平台全量/角色设计词_2001210035856343041.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `EmptyLatentImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `Text Multiline`
- `VAEDecode`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 6 | 100% |
| 高度 | 512 | 512 - 512 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
