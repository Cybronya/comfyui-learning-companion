---
name: unknown_workflow_video_lora_sampler_374
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.71325
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, GetNode, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/视频换脸，视频重绘（Wan2.1+Standin+Vace）_1965963887017455617.json, 视频生成/图生视频/Stand-In+VACE一致性视频生成_1958065173116366849.json, 视频生成/图生视频/Stand-In+VACE视频换脸_1959340354166272002.json, 视频生成/图生视频/Stand-In+vace高度人物一致性_1956763019890057217.json, 视频生成/图生视频/wan2.1+stand-in视频人像换脸_1957279872316010498.json, 视频生成/图生视频/👍最美最专角色姿态迁移+面部一致性视频生成工作流（VACE+stand-in）♥_1979202292152963074.json, 视频生成/图生视频/😍跳舞姿态迁移面部一致（VACE+stand-in）😍_1958798691941445634.json, 视频生成/文生视频/Wan2.1+姿势参考+Stand-In一致性文生视频_1956406110863458305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_374

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/视频换脸，视频重绘（Wan2.1+Standin+Vace）_1965963887017455617.json、视频生成/图生视频/Stand-In+VACE一致性视频生成_1958065173116366849.json、视频生成/图生视频/Stand-In+VACE视频换脸_1959340354166272002.json、视频生成/图生视频/Stand-In+vace高度人物一致性_1956763019890057217.json、视频生成/图生视频/wan2.1+stand-in视频人像换脸_1957279872316010498.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 8 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
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
- `SimpleMath+` —— 6/8 个有
- `WanVideoTorchCompileSettings` —— 6/8 个有
- `WanVideoVACEStartToEndFrame` —— 6/8 个有
- `AIO_Preprocessor` —— 5/8 个有
- `CR Text` —— 5/8 个有
- `INTConstant` —— 5/8 个有
- `ImageFromBatch+` —— 5/8 个有
- `ImpactInt` —— 4/8 个有
- `Anything Everywhere` —— 3/8 个有
- `ImageConcanate` —— 3/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `InspyrenetRembg` —— 3/8 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `OpenposePreprocessor` —— 3/8 个有
- `VHS_VideoInfo` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `easy imageRemBg` —— 2/8 个有
- `CM_IntToFloat` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `Int` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `MultiTalkModelLoader` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `Text` —— 1/8 个有
- `Text Concatenate` —— 1/8 个有
- `Wan22PromptSelector` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy imageScaleDownToSize` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
