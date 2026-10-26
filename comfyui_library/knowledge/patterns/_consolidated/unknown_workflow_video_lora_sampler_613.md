---
name: unknown_workflow_video_lora_sampler_613
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.678
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageResizeKJv2, LoadImage, SetNode, SimpleComparison+, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVAELoader, easy ifElse, easy int]
problems: []
missing: []
members: [视频生成/文生视频/SVI FILM 循环长视频_1984166711169581057.json, 视频生成/文生视频/SVI SHOT 长视频 循环_1984161219709992962.json, 视频生成/文生视频/SVI-SHOT 长视频 非循环_1984156029606920194.json, 视频生成/文生视频/SVI_FILM长视频生成_非循环_1984138847112069121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_613

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/SVI FILM 循环长视频_1984166711169581057.json、视频生成/文生视频/SVI SHOT 长视频 循环_1984161219709992962.json、视频生成/文生视频/SVI-SHOT 长视频 非循环_1984156029606920194.json、视频生成/文生视频/SVI_FILM长视频生成_非循环_1984138847112069121.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `SimpleComparison+`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEmbedBridge`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy ifElse`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `List of any [Crystools]` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `easy forLoopEnd` —— 2/4 个有
- `easy forLoopStart` —— 2/4 个有
- `easy indexAnything` —— 2/4 个有
- `easy lengthAnything` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
