---
name: unknown_workflow_video_lora_sampler_260
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.742
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Stand-In+VACE一致性视频生成_1958065173116366849.json, 视频生成/图生视频/Stand-In+VACE视频换脸_1959340354166272002.json, 视频生成/图生视频/Stand-In+vace高度人物一致性_1956763019890057217.json, 视频生成/图生视频/wan2.1+stand-in视频人像换脸_1957279872316010498.json, 视频生成/图生视频/自定义人脸_表情动作精准克隆_1957324783199383553.json, 视频生成/图生视频/视频生成视频_图生视频-动作迁移+人脸迁移-wan2.1_1958334806830551042.json, 视频生成/图生视频/👍最美最专角色姿态迁移+面部一致性视频生成工作流（VACE+stand-in）♥_1979202292152963074.json, 视频生成/图生视频/😍跳舞姿态迁移面部一致（VACE+stand-in）😍_1958798691941445634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_260

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Stand-In+VACE一致性视频生成_1958065173116366849.json、视频生成/图生视频/Stand-In+VACE视频换脸_1959340354166272002.json、视频生成/图生视频/Stand-In+vace高度人物一致性_1956763019890057217.json、视频生成/图生视频/wan2.1+stand-in视频人像换脸_1957279872316010498.json、视频生成/图生视频/自定义人脸_表情动作精准克隆_1957324783199383553.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
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
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `INTConstant` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `WanVideoTorchCompileSettings` —— 6/8 个有
- `CR Text` —— 5/8 个有
- `WanVideoVACEStartToEndFrame` —— 5/8 个有
- `ImageFromBatch+` —— 4/8 个有
- `ImpactInt` —— 4/8 个有
- `SimpleMath+` —— 4/8 个有
- `Anything Everywhere` —— 3/8 个有
- `ImageConcanate` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `InspyrenetRembg` —— 2/8 个有
- `Int` —— 2/8 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `OpenposePreprocessor` —— 2/8 个有
- `VHS_VideoInfo` —— 2/8 个有
- `easy imageRemBg` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `Evaluate Integers` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `easy convertAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
