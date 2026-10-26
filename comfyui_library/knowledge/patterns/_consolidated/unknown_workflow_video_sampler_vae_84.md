---
name: unknown_workflow_video_sampler_vae_84
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7535
common_nodes: [CR Text, GetNode, ImageConcatMulti, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewImage, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/三图参考-MAGREF图生视频_1935607588300193793.json, 视频生成/图生视频/单图参考-MAGREF图生视频_1935586332242530306.json, 视频生成/图生视频/单图参考-MAGREF图生视频_2055192187125682177.json, 视频生成/图生视频/双图参考-MAGREF图生视频_1935509475614707714.json, 视频生成/图生视频/视频-破次元融合版-多主体融合 FusionX-VACE_1934523459177250818.json, 视频生成/文生视频/wan2.1 MAGREF_FusionX 3倍加速图生视频_1938855885659627522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_84

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/三图参考-MAGREF图生视频_1935607588300193793.json、视频生成/图生视频/单图参考-MAGREF图生视频_1935586332242530306.json、视频生成/图生视频/单图参考-MAGREF图生视频_2055192187125682177.json、视频生成/图生视频/双图参考-MAGREF图生视频_1935509475614707714.json、视频生成/图生视频/视频-破次元融合版-多主体融合 FusionX-VACE_1934523459177250818.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CR Text`
- `GetNode`
- `ImageConcatMulti`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `WanVideoClipVisionEncode` —— 5/6 个有
- `WanVideoImageToVideoEncode` —— 5/6 个有
- `WanVideoLoraSelect` —— 5/6 个有
- `easy imageRemBg` —— 5/6 个有
- `GetImageSizeAndCount` —— 3/6 个有
- `ImageConcanate` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `AddLabel` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `easy imageScaleDownToSize` —— 2/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `InspyrenetRembg` —— 1/6 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/6 个有
- `WanVideoVACEEncode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
