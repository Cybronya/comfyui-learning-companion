---
name: unknown_workflow_upscale_clip_checkpoint_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.8
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Fast Groups Muter (rgthree), Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewAny, SaveImage, UltimateSDUpscale, UpscaleModelLoader, easy saveText, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/Qwen反推+SD放大工作流_2066818308095168514.json, 图片生成/图生图/Qwen反推+SD放大工作流_2067060715948695554.json, 图片生成/图生图/自用SD放大工作流_2004864597557477377.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen反推+SD放大工作流_2066818308095168514.json、图片生成/图生图/Qwen反推+SD放大工作流_2067060715948695554.json、图片生成/图生图/自用SD放大工作流_2004864597557477377.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
