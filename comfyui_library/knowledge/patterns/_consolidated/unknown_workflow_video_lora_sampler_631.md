---
name: unknown_workflow_video_lora_sampler_631
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.753
common_nodes: [CLIPVisionLoader, CR Text, GetNode, ImageConcatMulti, ImageResizeKJv2, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewImage, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/三图参考-MAGREF图生视频_1935607588300193793.json, 视频生成/图生视频/单图参考-MAGREF图生视频_1935586332242530306.json, 视频生成/图生视频/单图参考-MAGREF图生视频_2055192187125682177.json, 视频生成/图生视频/双图参考-MAGREF图生视频_1935509475614707714.json, 视频生成/文生视频/wan2.1 MAGREF_FusionX 3倍加速图生视频_1938855885659627522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_631

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/三图参考-MAGREF图生视频_1935607588300193793.json、视频生成/图生视频/单图参考-MAGREF图生视频_1935586332242530306.json、视频生成/图生视频/单图参考-MAGREF图生视频_2055192187125682177.json、视频生成/图生视频/双图参考-MAGREF图生视频_1935509475614707714.json、视频生成/文生视频/wan2.1 MAGREF_FusionX 3倍加速图生视频_1938855885659627522.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `easy imageScaleDownToSize` —— 2/5 个有
- `AddLabel` —— 1/5 个有
- `EmptyImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
