# Learning Records

> 分析工作流过程中新学到的节点/模型/原理记录。每条: [日期] 主题 — 要点 — 关联文件。

- [2026-10-04] ComfyUI PNG 元数据 — ComfyUI 生成/保存的 PNG 在 tEXt chunk 内嵌两份 JSON：`workflow`（UI 画布格式，含 nodes/links/坐标）与 `prompt`（API 格式，数字键 + class_type + inputs）。提取工具：`skills/comfyui-learning/tools/extract_png_workflow.py`（新增，标准库实现，覆盖 tEXt/iTXt/zTXt）。— 关联: workflows/sd1.5/text-to-image-workflow.png
- [2026-10-04] 核心节点六件套 — CheckpointLoaderSimple（一次输出 MODEL/CLIP/VAE 三路）、CLIPTextEncode（文本→CONDITIONING，正负各一）、EmptyLatentImage（空白潜空间起点）、KSampler（五要素：model/positive/negative/latent + seed/steps/cfg/sampler/scheduler/denoise）、VAEDecode（LATENT→IMAGE）、SaveImage。— 关联: knowledge/patterns/sd15-t2i-basic.md
- [2026-10-04] SD1.5 官方权重文件名 — `v1-5-pruned-emaonly-fp16.safetensors`：pruned=裁剪版（去掉训练优化器状态，体积小）、emaonly=只含 EMA 权重（出图更稳定）、fp16=半精度（显存约 2GB）。— 关联: workflows/sd1.5/text-to-image-workflow.png
- [2026-10-04] LoraLoader 注入点与双强度 — 插在 CheckpointLoader 之后、编码/采样之前，同时改写 MODEL 与 CLIP 两路（VAE 不经过它，仍直连底模）。strength_model 管画面风格幅度（实测 0.75），strength_clip 管触发词响应（实测 1.0）；>1.2 易崩坏，SD1.5 LoRA 不兼容 SDXL/Flux。— 关联: knowledge/summaries/loraloader.md, knowledge/patterns/sd15-t2i-lora.md
- [2026-10-04] SD1.5 采样参数进阶 — dpmpp_2m+karras 是高质量常用组合（实测 30 步/cfg 7）；负面词权重语法 `(worst quality, low quality:1.4)` 比裸列更有力；SD1.5 出图上限 768 系，再大易构图崩坏。— 关联: workflows/sd1.5/lora.png
- [2026-10-04] 工具坑 ×2 — ① `extract_png_workflow.py` 的输出文件 `_prompt.json`/`_workflow.json` 放在 workflows 目录里会被 `knowledge_builder.py --init-index` 当成两个独立工作流重复统计，产物应放别处或加排除；② `compare_workflow.py --index` 假定索引条目是 JSON，但 workflow_index.json 的 path 指向 PNG，直接跑会 JSONDecodeError，需先手动提取 JSON 再走双文件对比。— 关联: skills/comfyui-learning/tools/
