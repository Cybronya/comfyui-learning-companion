---
name: unknown_workflow_controlnet_video_lora_39
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9045
common_nodes: [CLIPVisionLoader, CR Text, Fast Groups Bypasser (rgthree), ImageResizeKJv2, ImpactSwitch, Int, LoadImage, LoadWanVideoT5TextEncoder, Note Plus (mtb), SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/Magref 全自动单图参考人物一致性视频生成 uni3c镜头控制+Lightx2v极速版_1937589913980440578.json, 视频生成/图生视频/Magref 双图参考人物一致性视频生成 uni3c镜头控制+闪电极速版-StarAI_1937919496172519425.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_39

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Magref 全自动单图参考人物一致性视频生成 uni3c镜头控制+Lightx2v极速版_1937589913980440578.json、视频生成/图生视频/Magref 双图参考人物一致性视频生成 uni3c镜头控制+闪电极速版-StarAI_1937919496172519425.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Note Plus (mtb)`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `easy globalSeed` —— 1/2 个有
- `easy imageScaleDownToSize` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
