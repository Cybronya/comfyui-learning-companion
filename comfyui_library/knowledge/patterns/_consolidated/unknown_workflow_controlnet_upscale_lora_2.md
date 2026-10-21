---
name: unknown_workflow_controlnet_upscale_lora_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.681667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, INTConstant, ImageScaleToTotalPixels, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/AA--Zimage参考文生图-controlnet-人物姿势_建筑构图等-基础_2006739441741733890.json, 图片生成/文生图/AA--批量洗图-Zimage controlnet精准洗图_生图+4K放大--批量版本_2005623741910581250.json, 图片生成/文生图/AA--洗图-Zimage controlnet精准自动洗图_生图+4K放大--单图版本_2001512031041798146.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/AA--Zimage参考文生图-controlnet-人物姿势_建筑构图等-基础_2006739441741733890.json、图片生成/文生图/AA--批量洗图-Zimage controlnet精准洗图_生图+4K放大--批量版本_2005623741910581250.json、图片生成/文生图/AA--洗图-Zimage controlnet精准自动洗图_生图+4K放大--单图版本_2001512031041798146.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Qwen3_VQA` —— 2/3 个有
- `easy saveText` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `RHBatchImages:` —— 1/3 个有
- `RHExtractImage` —— 1/3 个有
- `RHUploadZip` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy imageCount` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
