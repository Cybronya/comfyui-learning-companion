---
name: text_to_image_ipadapter_sampler_clip
type: Text To Image
frequency: 5
level: strong
coverage: 0.9734
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, IPAdapterUnifiedLoader, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/室内设计线稿一键上色还原场景_1891028825663246337.json, 图片生成/图生图/锁脸_2055695752340492290.json, 图片生成/文生图/SDXL版ipadapter_1979490298709577729.json, 视频生成/图生视频/ipadapter_faceid_workflow_2053664172625408002.json, 视频生成/图生视频/ipadapter_faceid_workflow_2053673513051013121.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_sampler_clip

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/室内设计线稿一键上色还原场景_1891028825663246337.json、图片生成/图生图/锁脸_2055695752340492290.json、图片生成/文生图/SDXL版ipadapter_1979490298709577729.json、视频生成/图生视频/ipadapter_faceid_workflow_2053664172625408002.json、视频生成/图生视频/ipadapter_faceid_workflow_2053673513051013121.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `IPAdapterAdvanced` —— 3/5 个有
- `Get Image Size (JPS)` —— 1/5 个有
- `IPAdapterFaceID` —— 1/5 个有
- `IPAdapterStyleComposition` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 896 - 1632 | 5 | 79% |
| 高度 | 1024 | 720 - 1152 | 5 | 80% |
| 采样步数 | 25 | 20 - 25 | 5 | 92% |
| Prompt 约束强度(CFG) | 7 | 5 - 8 | 5 | 84% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | karras | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 896 - 1632，5 个样本
- 高度 中位数 1024，观测区间 720 - 1152，5 个样本
- 采样步数 中位数 25，观测区间 20 - 25，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 5 - 8，5 个样本，取值集中（一致性 84%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 karras，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
