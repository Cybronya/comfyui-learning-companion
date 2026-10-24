---
name: unknown_workflow_video_lora_sampler_561
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.930667
common_nodes: [GetImageSize, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2-14B 图生视频 6s 短边720自适应_1956713305550065665.json, 视频生成/图生视频/wan 2.2 图生视频  kj 加速_1950010533321859074.json, 视频生成/图生视频/wan2.2图生视频api_1950068029456564225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_561

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Wan2.2-14B 图生视频 6s 短边720自适应_1956713305550065665.json、视频生成/图生视频/wan 2.2 图生视频  kj 加速_1950010533321859074.json、视频生成/图生视频/wan2.2图生视频api_1950068029456564225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSize`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
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
- `CreateCFGScheduleFloatList` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `LayerUtility: BooleanOperatorV2` —— 2/3 个有
- `LayerUtility: If ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy imageScaleDownToSize` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/3 个有
- `GIMMVFI_interpolate` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
