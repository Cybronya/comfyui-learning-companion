---
name: unknown_workflow_video_lora_sampler_631
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.889
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ImageScale, InstructPixToPixConditioning, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SamplerCustom, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan lora-depth控制 + 图片参考=civen_cn_1905283605348667393.json, 视频生成/图生视频/Wan2.1深度控制视频迁移和重绘_1903507443177918465.json, 视频生成/文生视频/Wan视频深度控制工作流-官方版_1904420884050776066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_631

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan lora-depth控制 + 图片参考=civen_cn_1905283605348667393.json、视频生成/图生视频/Wan2.1深度控制视频迁移和重绘_1903507443177918465.json、视频生成/文生视频/Wan视频深度控制工作流-官方版_1904420884050776066.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageScale`
- `InstructPixToPixConditioning`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SamplerCustom`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `DepthAnythingV2Preprocessor` —— 1/3 个有
- `DownloadAndLoadFlorence2Model` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `Primitive string [Crystools]` —— 1/3 个有
- `ReActorFaceSwap` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TeaCache` —— 1/3 个有
- `Text Concatenate (JPS)` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
