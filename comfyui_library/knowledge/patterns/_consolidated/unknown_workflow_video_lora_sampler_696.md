---
name: unknown_workflow_video_lora_sampler_696
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6275
common_nodes: [Anything Everywhere3, CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageCropByMaskAndResize, Int, LayerUtility: PurgeVRAM V2, LoadImage, MathExpression|pysssss, PixelPerfectResolution, Seed Everywhere, SetNode, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/动作迁移 Motion transfer WAN2.2 Animate_1975181614286286850.json, 平台全量/电商产品展示 参考视频动作表情 wan2.2 animate_2035232688927416322.json, 平台全量/视频服装替换 Video costume replacement WAN2.2 Animate_1980300071138975746.json, 平台全量/视频服装替换 Video costume replacement WAN2.2 Animate_2032833460196352001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_696

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/动作迁移 Motion transfer WAN2.2 Animate_1975181614286286850.json、平台全量/电商产品展示 参考视频动作表情 wan2.2 animate_2035232688927416322.json、平台全量/视频服装替换 Video costume replacement WAN2.2 Animate_1980300071138975746.json、平台全量/视频服装替换 Video costume replacement WAN2.2 Animate_2032833460196352001.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageCropByMaskAndResize`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MathExpression|pysssss`
- `PixelPerfectResolution`
- `Seed Everywhere`
- `SetNode`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `BlockifyMask` —— 2/4 个有
- `DrawMaskOnImage` —— 2/4 个有
- `DuckHideNode` —— 2/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `LayerMask: SegformerClothesPipelineLoader` —— 2/4 个有
- `LayerMask: SegformerUltraV2` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `TT_img_enc_v2` —— 2/4 个有
- `easy anythingIndexSwitch` —— 2/4 个有
- `easy imageRemBg` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `WanVideoEncode` —— 1/4 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/4 个有
- `WanVideoUni3C_embeds` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
