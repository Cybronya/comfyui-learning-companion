---
name: unknown_workflow_video_lora_sampler_764
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.784667
common_nodes: [AIO_Preprocessor, ApplyFaceProcessor, FaceProcessorLoader, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/自定义人脸_表情动作精准克隆_1957324783199383553.json, 视频生成/图生视频/视频生成视频_图生视频-动作迁移+人脸迁移-wan2.1_1958334806830551042.json, 视频生成/文生视频/03-12-02-WAN2.1-参考人物视频转绘-Standin+Vace_1989933948379820033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_764

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/自定义人脸_表情动作精准克隆_1957324783199383553.json、视频生成/图生视频/视频生成视频_图生视频-动作迁移+人脸迁移-wan2.1_1958334806830551042.json、视频生成/文生视频/03-12-02-WAN2.1-参考人物视频转绘-Standin+Vace_1989933948379820033.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `Evaluate Integers` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy convertAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
