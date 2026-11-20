---
name: unknown_workflow_video_lora_sampler_211
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.799
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wanvideo_Stand-In角色一致性工作流_1956293638198362114.json, 视频生成/图生视频/角色一致性图生视频_1973164651716415490.json, 视频生成/图生视频/🥝stand-in脸部一致性视频生成 文生视频🥝_1956266863963590657.json, 视频生成/文生视频/03-12-01-WAN2.1-脸部参考文生视频-Standin_1989933889823100930.json, 视频生成/文生视频/Aiwood-Stand-id+vace控制版_1955702074303397890.json, 视频生成/文生视频/Aiwood-Stand-id无控制板_1955698165593751554.json, 视频生成/文生视频/Stand In+Aniwan脸部参考文生视频V1 （高动态版）_1956789708207394817.json, 视频生成/文生视频/Stand In+Vace姿势参考脸部一致性视频生成V1_1956763443317628929.json, 视频生成/文生视频/Stand In脸部参考文生视频V1_1956768845814796289.json, 视频生成/文生视频/Wan面部参考+动作参考Stand-in文生视频_1957506592558215169.json, 视频生成/文生视频/文生视频stand-in脸部保持一致性视频生成_1957446441918722049.json, 视频生成/文生视频/🥝stand-in脸部一致性视频生成 VACE姿态迁移版🥝_1956266838781034498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_211

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/wanvideo_Stand-In角色一致性工作流_1956293638198362114.json、视频生成/图生视频/角色一致性图生视频_1973164651716415490.json、视频生成/图生视频/🥝stand-in脸部一致性视频生成 文生视频🥝_1956266863963590657.json、视频生成/文生视频/03-12-01-WAN2.1-脸部参考文生视频-Standin_1989933889823100930.json、视频生成/文生视频/Aiwood-Stand-id+vace控制版_1955702074303397890.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 12 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
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
- `ImageResizeKJv2` —— 10/12 个有
- `WanVideoEmptyEmbeds` —— 10/12 个有
- `easy imageRemBg` —— 10/12 个有
- `INTConstant` —— 9/12 个有
- `WanVideoVACEModelSelect` —— 9/12 个有
- `ImageConcanate` —— 8/12 个有
- `CR Text` —— 7/12 个有
- `WanVideoTorchCompileSettings` —— 7/12 个有
- `ImpactInt` —— 6/12 个有
- `OpenposePreprocessor` —— 5/12 个有
- `PreviewImage` —— 5/12 个有
- `VHS_LoadVideo` —— 5/12 个有
- `WanVideoVACEEncode` —— 5/12 个有
- `WanVideoVACEStartToEndFrame` —— 5/12 个有
- `GetNode` —— 4/12 个有
- `ImageConcatMulti` —— 4/12 个有
- `SetNode` —— 4/12 个有
- `JWInteger` —— 3/12 个有
- `SimpleMath+` —— 3/12 个有
- `Label (rgthree)` —— 2/12 个有
- `Note Plus (mtb)` —— 2/12 个有
- `ImpactSwitch` —— 1/12 个有
- `JjkText` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
