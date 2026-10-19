---
name: unknown_workflow_video_sampler_clip_38
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.844417
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImpactSwitch, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/1981232802555486209.json, 视频生成/图生视频/1979840137557348353.json, 视频生成/图生视频/1980202045699428353.json, 视频生成/图生视频/1979756399754383362.json, 视频生成/图生视频/1979756565743964162.json, 视频生成/图生视频/1950101403698159617.json, 视频生成/图生视频/1989139978758262786.json, 视频生成/图生视频/1988842401047392257.json, 视频生成/图生视频/2050784793184481281.json, 视频生成/图生视频/2052282048966082561.json, 视频生成/图生视频/2075852358004862978.json, 视频生成/图生视频/1995538932051927042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1981232802555486209.json、视频生成/图生视频/1979840137557348353.json、视频生成/图生视频/1980202045699428353.json、视频生成/图生视频/1979756399754383362.json、视频生成/图生视频/1979756565743964162.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImpactSwitch`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ModelPatchTorchSettings` —— 11/12 个有
- `ShowText|pysssss` —— 11/12 个有
- `Text Concatenate` —— 11/12 个有
- `Wan22PromptSelector` —— 11/12 个有
- `ImageStitch` —— 9/12 个有
- `PrimitiveInt` —— 9/12 个有
- `PrimitiveStringMultiline` —— 9/12 个有
- `LoraLoaderModelOnly` —— 8/12 个有
- `ImageResizeKJv2` —— 7/12 个有
- `ImageBatchMulti` —— 6/12 个有
- `ImageConcatMulti` —— 6/12 个有
- `ImageScaleToTotalPixels` —— 6/12 个有
- `WanMultiFrameRefToVideo` —— 6/12 个有
- `WanImageToVideo` —— 4/12 个有
- `CR Text` —— 3/12 个有
- `GetNode` —— 3/12 个有
- `JWInteger` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `easy showAnything` —— 3/12 个有
- `ImageConcanate` —— 2/12 个有
- `WanFirstLastFrameToVideo` —— 2/12 个有
- `GetImageSizeAndCount` —— 1/12 个有
- `ImageResizeKJ` —— 1/12 个有
- `RIFE VFI` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `TT_img_enc` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 100% |
| Prompt 约束强度(CFG) | 7 | 4 - 8 | 12 | 81% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler_ancestral | - | 12 | 92% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 4 - 8，12 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，12 个样本，一致性 92%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
