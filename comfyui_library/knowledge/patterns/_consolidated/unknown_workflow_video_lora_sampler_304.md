---
name: unknown_workflow_video_lora_sampler_304
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.92125
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, LoadImage, LoadWanVideoT5TextEncoder, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Stand In Face Swap换脸_1960243766210801666.json, 视频生成/图生视频/Stand In Face Swap视频换脸V2（背景洗图版）_1956781749314228225.json, 视频生成/图生视频/Stand-In超级人物一致性图生视频_1956951152292192258.json, 视频生成/图生视频/Stand-In身份一致性参考视频_1955673336359653378.json, 视频生成/图生视频/Stand-In面部参考生成视频_1956191796604882946.json, 视频生成/图生视频/stand in 视频换脸+视频高清放大V1_1959190374550024194.json, 视频生成/图生视频/（自用）Stand In Face Swap视频换脸V2（背景洗图版）_1958204271017791490.json, 视频生成/文生视频/（自用）Stand In Face Swap视频换脸V2_1956898077279969282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_304

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Stand In Face Swap换脸_1960243766210801666.json、视频生成/图生视频/Stand In Face Swap视频换脸V2（背景洗图版）_1956781749314228225.json、视频生成/图生视频/Stand-In超级人物一致性图生视频_1956951152292192258.json、视频生成/图生视频/Stand-In身份一致性参考视频_1955673336359653378.json、视频生成/图生视频/Stand-In面部参考生成视频_1956191796604882946.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/8 个有
- `VHS_VideoCombine` —— 7/8 个有
- `CR Prompt Text` —— 5/8 个有
- `JWInteger` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `VHS_LoadVideo` —— 5/8 个有
- `VideoInputPreprocessor` —— 5/8 个有
- `ImageConcatMulti` —— 4/8 个有
- `VHS_VideoInfo` —— 4/8 个有
- `Primitive integer [Crystools]` —— 3/8 个有
- `WanVideoTorchCompileSettings` —— 3/8 个有
- `LatentLoaderAdvanced` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `SaveLatent` —— 2/8 个有
- `FaceOnlyModeSwitch` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `ReActorFaceSwap` —— 1/8 个有
- `SeedVR2` —— 1/8 个有
- `VHS_VideoInfoLoaded` —— 1/8 个有
- `VideoBackgroundRestorer` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
