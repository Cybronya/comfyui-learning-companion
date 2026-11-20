---
name: unknown_workflow_video_lora_sampler_1076
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [AIO_Preprocessor, BasicScheduler, CLIPLoader, CLIPTextEncode, ImageResizeKJ, ImageScale, InstructPixToPixConditioning, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SamplerCustom, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan lora-depth控制 + 图片参考=civen_cn_1905283605348667393.json, 视频生成/文生视频/Wan视频深度控制工作流-官方版_1904420884050776066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1076

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan lora-depth控制 + 图片参考=civen_cn_1905283605348667393.json、视频生成/文生视频/Wan视频深度控制工作流-官方版_1904420884050776066.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJ`
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
- `DeepTranslatorTextNode` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `ReActorFaceSwap` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TeaCache` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
