---
name: image_to_image_sampler_clip_unet_26
type: Image To Image
frequency: 2
level: weak
coverage: 0.9615
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image Base 图像放大细节修复ComfyUI工作流_2033567937352704002.json, 视频生成/图生视频/2038098911314841602.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image Base 图像放大细节修复ComfyUI工作流_2033567937352704002.json、视频生成/图生视频/2038098911314841602.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningClamp` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Textbox` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有
- `image_scale_pixel_v2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 67% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.45 | - | 2 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.45，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
