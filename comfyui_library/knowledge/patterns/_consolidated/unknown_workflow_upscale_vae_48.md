---
name: unknown_workflow_upscale_vae_48
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.846
common_nodes: [BOOLConstant, ComfyUI_Image_Round__ImageCropAdvanced, DisplayAny, DualCLIPLoader, GetImageSize, ImageUpscaleWithModel, JoinStrings, KOOK_SaveJPGImage, LoadImage, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Gemini31Flash, SimpleMath+, Text Input [Dream], UpscaleModelLoader, VAELoader, easy ifElse, easy imageSplitGrid]
problems: []
missing: []
members: [图片生成/图生图/一键换衣+4pose展示_2079549439529807874.json, 图片生成/图生图/配饰工作流_2076518830742007809.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_48

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键换衣+4pose展示_2079549439529807874.json、图片生成/图生图/配饰工作流_2076518830742007809.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BOOLConstant`
- `ComfyUI_Image_Round__ImageCropAdvanced`
- `DisplayAny`
- `DualCLIPLoader`
- `GetImageSize`
- `ImageUpscaleWithModel`
- `JoinStrings`
- `KOOK_SaveJPGImage`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Gemini31Flash`
- `SimpleMath+`
- `Text Input [Dream]`
- `UpscaleModelLoader`
- `VAELoader`
- `easy ifElse`
- `easy imageSplitGrid`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
