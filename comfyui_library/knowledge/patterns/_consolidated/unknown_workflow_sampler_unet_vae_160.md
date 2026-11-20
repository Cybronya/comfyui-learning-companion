---
name: unknown_workflow_sampler_unet_vae_160
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.98
common_nodes: [BasicGuider, CLIPLoader, RandomNoise, SamplerCustomAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json, 图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json, 图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json, 图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json, 平台全量/Qwen Image 2.1 Turbo 分镜生图（场景） V20261018_2117325048951431169.json, 平台全量/Qwen Image 2.1 Turbo 分镜生图（角色+场景） V20261018_2117325895718498305.json, 平台全量/Qwen Image 2.1 Turbo 单图编辑 V20261018_2117486305058836481.json, 平台全量/Qwen Image 2.1 Turbo 多图编辑 1080P（原映射）V20261027_2117329747205255170.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_160

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json、图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json、图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json、图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json、平台全量/Qwen Image 2.1 Turbo 分镜生图（场景） V20261018_2117325048951431169.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `SaveImage` —— 6/8 个有
- `SaveImageAdvanced` —— 6/8 个有
- `EmptyLatentImage` —— 5/8 个有
- `CR Prompt Text` —— 4/8 个有
- `KSamplerSelect` —— 4/8 个有
- `ManualSigmas` —— 4/8 个有
- `QwenImage21FunPDDLoader` —— 4/8 个有
- `easy int` —— 4/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `PrimitiveInt` —— 2/8 个有
- `ImageScale` —— 1/8 个有
- `QwenImage21Cache` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
