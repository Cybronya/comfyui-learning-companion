---
name: text_to_image_sampler_clip_unet_153
type: Text To Image
frequency: 2
level: weak
coverage: 0.7315
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LayerUtility: PurgeVRAM, LoadImage, PreviewImage, Qwen3_VQA, RHBatchImages:, RHExtractImage, RHUploadZip, SaveImage, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/AA-单图 _ 批量洗图--QWEN反推--Zimage生图+4K超清放大_2003824572606652418.json, 图片生成/文生图/Z-image，文生图新王，批量洗图工作流_1994368804329299969.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_153

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/AA-单图 _ 批量洗图--QWEN反推--Zimage生图+4K超清放大_2003824572606652418.json、图片生成/文生图/Z-image，文生图新王，批量洗图工作流_1994368804329299969.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PreviewImage`
- `Qwen3_VQA`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AspectRatio` —— 1/2 个有
- `Bjornulf_ShowInt` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy saveText` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
