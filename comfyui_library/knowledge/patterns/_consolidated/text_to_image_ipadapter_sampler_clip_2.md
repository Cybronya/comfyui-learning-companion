---
name: text_to_image_ipadapter_sampler_clip_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.713
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, IPAdapterFaceID, IPAdapterUnifiedLoaderFaceID, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/lora面部训练_2056047508161343489.json, 图片生成/文生图/文生图参考脸部ipadapter_faceid_1916072678388596738.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/lora面部训练_2056047508161343489.json、图片生成/文生图/文生图参考脸部ipadapter_faceid_1916072678388596738.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `IPAdapterFaceID`
- `IPAdapterUnifiedLoaderFaceID`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `> Text` —— 1/2 个有
- `> Text Combine` —— 1/2 个有
- `> Text Pick Line by Index` —— 1/2 个有
- `CounterNode` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.75 | - | 2 | 96% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.75，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
