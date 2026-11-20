---
name: unknown_workflow_controlnet_video_lora_34
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.916667
common_nodes: [CLIPVisionLoader, Fast Groups Bypasser (rgthree), ImageResizeKJv2, Int, LoadImage, LoadWanVideoT5TextEncoder, Note Plus (mtb), SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: ["平台全量/Magref 三图参考人物一致性视频生成,智能描述极速版-StarAI_1938191803185020930.json", 视频生成/图生视频/Magref 全自动单图参考人物一致性视频生成 uni3c镜头控制+Lightx2v极速版_1937589913980440578.json, 视频生成/图生视频/Magref 双图参考人物一致性视频生成 uni3c镜头控制+闪电极速版-StarAI_1937919496172519425.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_34

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Magref 三图参考人物一致性视频生成,智能描述极速版-StarAI_1938191803185020930.json、视频生成/图生视频/Magref 全自动单图参考人物一致性视频生成 uni3c镜头控制+Lightx2v极速版_1937589913980440578.json、视频生成/图生视频/Magref 双图参考人物一致性视频生成 uni3c镜头控制+闪电极速版-StarAI_1937919496172519425.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
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
- `CR Text` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `easy imageScaleDownToSize` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy globalSeed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
