---
name: unknown_workflow_lora_sampler_clip_198
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.884
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ComfyMathExpression, ComfySwitchNode, ContextWindowsManual, CreateVideo, GetImageSize, GetVideoComponents, ImageFromBatch, ImageStitch, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PrimitiveBoolean, ResizeImageMaskNode, SamplerCustom, SaveVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoInfoLoaded, WanAnimate2Cache, WanAnimate2ToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan Animate 2 动作迁移_2089624498260766721.json, 视频生成/图生视频/WanAnimate2 高清动作迁移人物角色替换V9_2100484560789270529.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_198

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan Animate 2 动作迁移_2089624498260766721.json、视频生成/图生视频/WanAnimate2 高清动作迁移人物角色替换V9_2100484560789270529.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ContextWindowsManual`
- `CreateVideo`
- `GetImageSize`
- `GetVideoComponents`
- `ImageFromBatch`
- `ImageStitch`
- `KSamplerSelect`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PrimitiveBoolean`
- `ResizeImageMaskNode`
- `SamplerCustom`
- `SaveVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanAnimate2Cache`
- `WanAnimate2ToVideo`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
