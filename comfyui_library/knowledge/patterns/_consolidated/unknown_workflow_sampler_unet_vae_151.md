---
name: unknown_workflow_sampler_unet_vae_151
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96
common_nodes: [BasicGuider, CLIPLoader, QwenImage21FunPDDLoader, RandomNoise, SamplerCustomAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json, 图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json, 图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json, 图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_151

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json、图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json、图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json、图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `QwenImage21FunPDDLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `PrimitiveInt` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `SaveImageAdvanced` —— 2/4 个有
- `EmptyLatentImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
