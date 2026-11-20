---
name: unknown_workflow_video_lora_sampler_503
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9706
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2_2_i2v_KJ工作流_blockexample_1962483006248235010.json, 视频生成/图生视频/gen全能视频Si-wan2.2首尾帧kijai版_1952803879810494466.json, 视频生成/图生视频/kijai-Wan2.2首尾帧+过渡帧_1963047092535136257.json, 视频生成/图生视频/wan2.2图生视频_1961798280172781569.json, 视频生成/图生视频/视频-Wan2.2首尾帧+过渡帧_1978365294227906562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_503

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2_2_i2v_KJ工作流_blockexample_1962483006248235010.json、视频生成/图生视频/gen全能视频Si-wan2.2首尾帧kijai版_1952803879810494466.json、视频生成/图生视频/kijai-Wan2.2首尾帧+过渡帧_1963047092535136257.json、视频生成/图生视频/wan2.2图生视频_1961798280172781569.json、视频生成/图生视频/视频-Wan2.2首尾帧+过渡帧_1978365294227906562.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/5 个有
- `LoadWanVideoClipTextEncoder` —— 2/5 个有
- `WanVideoClipVisionEncode` —— 2/5 个有
- `WanVideoContextOptions` —— 2/5 个有
- `WanVideoEncodeLatentBatch` —— 2/5 个有
- `JWInteger` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `TT_img_enc` —— 1/5 个有
- `Textbox` —— 1/5 个有
- `WanVideoApplyNAG` —— 1/5 个有
- `WanVideoLoraBlockEdit` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
