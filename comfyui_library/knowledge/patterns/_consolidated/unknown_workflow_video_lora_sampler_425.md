---
name: unknown_workflow_video_lora_sampler_425
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.832429
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/StandIn视频换脸_1959200200009134081.json, 视频生成/图生视频/Stand-In超级人物一致性图生视频_1956951152292192258.json, 视频生成/图生视频/Stand-In身份一致性参考视频_1955673336359653378.json, 视频生成/图生视频/Stand-In面部参考生成视频_1956191796604882946.json, 视频生成/图生视频/wanvideo_Stand-In_人脸一致性_1959331317118873601.json, 视频生成/文生视频/StandIn人物一致性_1959187908609650689.json, 视频生成/文生视频/Wan2.2Stand-in视频面部交换实战_2004807686212513794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_425

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/StandIn视频换脸_1959200200009134081.json、视频生成/图生视频/Stand-In超级人物一致性图生视频_1956951152292192258.json、视频生成/图生视频/Stand-In身份一致性参考视频_1955673336359653378.json、视频生成/图生视频/Stand-In面部参考生成视频_1956191796604882946.json、视频生成/图生视频/wanvideo_Stand-In_人脸一致性_1959331317118873601.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 6/7 个有
- `WanVideoSetLoRAs` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `Primitive integer [Crystools]` —— 3/7 个有
- `FaceOnlyModeSwitch` —— 2/7 个有
- `GetImageSize+` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `VideoInputPreprocessor` —— 2/7 个有
- `CreateCFGScheduleFloatList` —— 1/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `VideoBackgroundRestorer` —— 1/7 个有
- `VideoFramePreprocessor` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
