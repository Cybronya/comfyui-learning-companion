---
name: image_to_image_sampler_clip_unet_12
type: Image To Image
frequency: 2
level: weak
coverage: 0.926
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/图生视频/2038098911314841602.json, 视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2038098911314841602.json、视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 1/2 个有
- `Qwen3VLProcessor` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `VAELoaderKJ` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 34 | - | 2 | 82% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 89% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.725 | - | 2 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 34，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.725，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
