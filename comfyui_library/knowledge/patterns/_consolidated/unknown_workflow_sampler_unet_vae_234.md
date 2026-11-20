---
name: unknown_workflow_sampler_unet_vae_234
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.93
common_nodes: [EmptyLatentImage, KSampler, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_KolorsUNETLoaderV2, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Kolors文生图_1930423082354163713.json, 图片生成/文生图/Kolors文生图工作流_1817854434880958465.json, 图片生成/文生图/【遇见AI】可灵Kolors文生图基础工作流_2038459039100702721.json, 平台全量/Kolors模型+IPAdapter工作流_1819192928425148417.json, 平台全量/【遇见AI】可灵Kolors Ipadapter风格迁移_2038475559570776066.json, 平台全量/【遇见AI】可灵Kolors faceid换脸_2038530587874562049.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_234

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Kolors文生图_1930423082354163713.json、图片生成/文生图/Kolors文生图工作流_1817854434880958465.json、图片生成/文生图/【遇见AI】可灵Kolors文生图基础工作流_2038459039100702721.json、平台全量/Kolors模型+IPAdapter工作流_1819192928425148417.json、平台全量/【遇见AI】可灵Kolors Ipadapter风格迁移_2038475559570776066.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `EmptyLatentImage`
- `KSampler`
- `MZ_ChatGLM3Loader`
- `MZ_ChatGLM3_V2`
- `MZ_KolorsUNETLoaderV2`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/6 个有
- `MZ_IPAdapterModelLoaderKolors` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `JjkText` —— 2/6 个有
- `MZ_IPAdapterAdvancedKolors` —— 2/6 个有
- `MZ_KolorsCLIPVisionLoader` —— 2/6 个有
- `CLIPVisionLoader` —— 1/6 个有
- `MZ_IPAdapterFaceID` —— 1/6 个有
- `MZ_IPAdapterInsightFaceLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 5 | 6 | 95% |
| 采样算法 | euler_ancestral | - | 6 | 50% |
| 调度器 | normal | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 768 | 768 - 1024 | 6 | 87% |
| 高度 | 1024 | 1024 - 1280 | 6 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 5，6 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 50%
- 调度器 最常用 normal，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1024，6 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1280，6 个样本，取值集中（一致性 91%）
