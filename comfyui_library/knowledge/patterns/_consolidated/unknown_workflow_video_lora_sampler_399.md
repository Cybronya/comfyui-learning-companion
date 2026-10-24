---
name: unknown_workflow_video_lora_sampler_399
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8832
common_nodes: [CLIPVisionLoader, ImageBatchMulti, ImageResizeKJv2, InvertMask, LoadImage, LoadWanVideoT5TextEncoder, MaskBatchMulti, VHS_VideoCombine, WanVideoAddBindweaveEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncodeLatentBatch, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/BindWeave-图生视频-高人物一致性-双人角色（推荐）_1990706002230218754.json, 视频生成/图生视频/BindWeave_Multi-多图参考生成视频_1991713227203620865.json, 视频生成/图生视频/BindWeave_Multi-多图参考生成视频_1992107841632923649.json, 视频生成/图生视频/BindWeave三图参考图生视频V1(FPS16)_1989682113672867842.json, 视频生成/图生视频/BindWeave双图参考图生视频V1(FPS16)_1989682080592351234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_399

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/BindWeave-图生视频-高人物一致性-双人角色（推荐）_1990706002230218754.json、视频生成/图生视频/BindWeave_Multi-多图参考生成视频_1991713227203620865.json、视频生成/图生视频/BindWeave_Multi-多图参考生成视频_1992107841632923649.json、视频生成/图生视频/BindWeave三图参考图生视频V1(FPS16)_1989682113672867842.json、视频生成/图生视频/BindWeave双图参考图生视频V1(FPS16)_1989682080592351234.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `InvertMask`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskBatchMulti`
- `VHS_VideoCombine`
- `WanVideoAddBindweaveEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncodeLatentBatch`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `easy imageRemBg` —— 4/5 个有
- `CLIPLoader` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `SolidMask` —— 3/5 个有
- `TextImageEncodeQwenVL` —— 3/5 个有
- `WanVideoSetLoRAs` —— 3/5 个有
- `DrawMaskOnImage` —— 2/5 个有
- `ImageRemoveBackground+` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `TextInput_` —— 2/5 个有
- `TransparentBGSession+` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `DF_Text_Box` —— 1/5 个有
- `ImagePadKJ` —— 1/5 个有
- `MaskPreview` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `math_calculate` —— 1/5 个有
- `ttN seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
