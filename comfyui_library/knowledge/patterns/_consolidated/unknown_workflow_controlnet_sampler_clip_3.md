---
name: unknown_workflow_controlnet_sampler_clip_3
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.819625
common_nodes: [CLIPLoader, CLIPTextEncode, Canny, ConditioningZeroOut, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image Controlnet Union2.0+Inpaint局部重绘多重控制洗图_2000538829650096130.json, 图片生成/图生图/Z-image Controlnet Union2.0局部重绘-洗图_2001297848824102914.json, 图片生成/图生图/Z-image Controlnet Union2.0局部重绘-洗图_2001863501805174785.json, 图片生成/图生图/Z-image图生图-LineArt艺术线控制_1998929676905144321.json, 图片生成/图生图/Z-image标准版Cn控制V1图生图_1996307091344211970.json, 图片生成/图生图/（可彩图）Z-image_Controlnet_Union2.0+Inpaint局部重绘洗图_2000660090866855937.json, 图片生成/图生图/（自用）Z-image Controlnet Union2.0+Inpaint局部重绘洗图_2000610350284275714.json, 平台全量/Z-image Controlnet Union2.0+Inpaint 局部重绘多重控制_2001156164677234689.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-image Controlnet Union2.0+Inpaint局部重绘多重控制洗图_2000538829650096130.json、图片生成/图生图/Z-image Controlnet Union2.0局部重绘-洗图_2001297848824102914.json、图片生成/图生图/Z-image Controlnet Union2.0局部重绘-洗图_2001863501805174785.json、图片生成/图生图/Z-image图生图-LineArt艺术线控制_1998929676905144321.json、图片生成/图生图/Z-image标准版Cn控制V1图生图_1996307091344211970.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Canny`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `AIO_Preprocessor` —— 6/8 个有
- `EmptySD3LatentImage` —— 6/8 个有
- `GetImageSize` —— 6/8 个有
- `GrowMaskWithBlur` —— 6/8 个有
- `ImageAndMaskPreview_UTK` —— 6/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `InpaintModelConditioning` —— 6/8 个有
- `SetLatentNoiseMask` —— 6/8 个有
- `easy anythingIndexSwitch` —— 6/8 个有
- `ImageScaleToMaxDimension` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `TT_img_enc_v2` —— 2/8 个有
- `easy int` —— 2/8 个有
- `DuckHideNode` —— 1/8 个有
- `ImageBlend` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `LineArtPreprocessor` —— 1/8 个有
- `MaskToImage` —— 1/8 个有
- `TT_img_enc` —— 1/8 个有
- `easy imagePixelPerfect` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 8 | 97% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | res_multistep | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，8 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
