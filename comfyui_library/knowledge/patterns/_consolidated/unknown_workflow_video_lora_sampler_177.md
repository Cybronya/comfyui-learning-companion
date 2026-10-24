---
name: unknown_workflow_video_lora_sampler_177
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.792091
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/🥝stand-in脸部一致性视频生成 文生视频🥝_1956266863963590657.json, 视频生成/文生视频/03-12-01-WAN2.1-脸部参考文生视频-Standin_1989933889823100930.json, 视频生成/文生视频/03-12-02-WAN2.1-参考人物视频转绘-Standin+Vace_1989933948379820033.json, 视频生成/文生视频/Aiwood-Stand-id+vace控制版_1955702074303397890.json, 视频生成/文生视频/Aiwood-Stand-id无控制板_1955698165593751554.json, 视频生成/文生视频/Stand In+Aniwan脸部参考文生视频V1 （高动态版）_1956789708207394817.json, 视频生成/文生视频/Stand In+Vace姿势参考脸部一致性视频生成V1_1956763443317628929.json, 视频生成/文生视频/Stand In脸部参考文生视频V1_1956768845814796289.json, 视频生成/文生视频/Wan面部参考+动作参考Stand-in文生视频_1957506592558215169.json, 视频生成/文生视频/文生视频stand-in脸部保持一致性视频生成_1957446441918722049.json, 视频生成/文生视频/🥝stand-in脸部一致性视频生成 VACE姿态迁移版🥝_1956266838781034498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_177

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/🥝stand-in脸部一致性视频生成 文生视频🥝_1956266863963590657.json、视频生成/文生视频/03-12-01-WAN2.1-脸部参考文生视频-Standin_1989933889823100930.json、视频生成/文生视频/03-12-02-WAN2.1-参考人物视频转绘-Standin+Vace_1989933948379820033.json、视频生成/文生视频/Aiwood-Stand-id+vace控制版_1955702074303397890.json、视频生成/文生视频/Aiwood-Stand-id无控制板_1955698165593751554.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 11 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoVACEModelSelect` —— 10/11 个有
- `easy imageRemBg` —— 10/11 个有
- `INTConstant` —— 8/11 个有
- `ImageConcanate` —— 8/11 个有
- `WanVideoEmptyEmbeds` —— 8/11 个有
- `CR Text` —— 7/11 个有
- `ImpactInt` —— 6/11 个有
- `VHS_LoadVideo` —— 6/11 个有
- `WanVideoTorchCompileSettings` —— 6/11 个有
- `WanVideoVACEEncode` —— 6/11 个有
- `OpenposePreprocessor` —— 5/11 个有
- `WanVideoVACEStartToEndFrame` —— 5/11 个有
- `ImageConcatMulti` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `GetNode` —— 3/11 个有
- `JWInteger` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `SimpleMath+` —— 3/11 个有
- `Note Plus (mtb)` —— 2/11 个有
- `AIO_Preprocessor` —— 1/11 个有
- `ImpactSwitch` —— 1/11 个有
- `JjkText` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
