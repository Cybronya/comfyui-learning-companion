# Learning Records

> 分析工作流过程中新学到的节点/模型/原理记录。每条: [日期] 主题 — 要点 — 关联文件。

- [2026-10-04] ComfyUI PNG 元数据 — ComfyUI 生成/保存的 PNG 在 tEXt chunk 内嵌两份 JSON：`workflow`（UI 画布格式，含 nodes/links/坐标）与 `prompt`（API 格式，数字键 + class_type + inputs）。提取工具：`skills/comfyui-learning/tools/extract_png_workflow.py`（新增，标准库实现，覆盖 tEXt/iTXt/zTXt）。— 关联: workflows/sd1.5/text-to-image-workflow.png
- [2026-10-04] 核心节点六件套 — CheckpointLoaderSimple（一次输出 MODEL/CLIP/VAE 三路）、CLIPTextEncode（文本→CONDITIONING，正负各一）、EmptyLatentImage（空白潜空间起点）、KSampler（五要素：model/positive/negative/latent + seed/steps/cfg/sampler/scheduler/denoise）、VAEDecode（LATENT→IMAGE）、SaveImage。— 关联: knowledge/patterns/sd15-t2i-basic.md
- [2026-10-04] SD1.5 官方权重文件名 — `v1-5-pruned-emaonly-fp16.safetensors`：pruned=裁剪版（去掉训练优化器状态，体积小）、emaonly=只含 EMA 权重（出图更稳定）、fp16=半精度（显存约 2GB）。— 关联: workflows/sd1.5/text-to-image-workflow.png
