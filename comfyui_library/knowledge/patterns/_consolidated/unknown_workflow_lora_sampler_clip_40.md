---
name: unknown_workflow_lora_sampler_clip_40
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.9865
common_nodes: [BasicScheduler, CLIPTextEncode, CM_FloatToInt, CR Text, DualCLIPLoader, ImageConcanate, KSamplerSelect, LTXVAddGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, SamplerCustom, UNETLoader, VAEDecode, VAEEncode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/2052776354835386370.json, 视频生成/图生视频/2053463786572529666.json, 视频生成/图生视频/2053043034979356673.json, 视频生成/图生视频/2053027400342097921.json, 视频生成/图生视频/2053455525341343746.json, 视频生成/图生视频/2054000800241856513.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2052776354835386370.json、视频生成/图生视频/2053463786572529666.json、视频生成/图生视频/2053043034979356673.json、视频生成/图生视频/2053027400342097921.json、视频生成/图生视频/2053455525341343746.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `DualCLIPLoader`
- `ImageConcanate`
- `KSamplerSelect`
- `LTXVAddGuide`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 5/6 个有
- `DuckHideNode` —— 1/6 个有
- `Float to Int` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `TT_img_enc` —— 1/6 个有
- `TT_img_enc_v2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
