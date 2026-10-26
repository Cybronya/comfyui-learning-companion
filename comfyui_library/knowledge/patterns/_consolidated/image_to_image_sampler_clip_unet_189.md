---
name: image_to_image_sampler_clip_unet_189
type: Image To Image
frequency: 2
level: weak
coverage: 0.9585
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image Base 图像放大细节修复ComfyUI工作流_2033567937352704002.json, 图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_2114241540112601090.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_189

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image Base 图像放大细节修复ComfyUI工作流_2033567937352704002.json、图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_2114241540112601090.json）

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
- `EmptyImage` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Textbox` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.575 | - | 2 | 26% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.575，样本不足，未给区间，2 个样本，取值分散，一致性仅 26%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
