---
name: unknown_workflow_sampler_clip_vae_52
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94975
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen3.5+Klein AI 短剧漫剧｜自动写剧情一键出九宫格分镜_2046582075771326466.json, 图片生成/图生图/klein双图_2017158118563647490.json, 图片生成/文生图/klein_文生图+图像编辑_2042538360702509058.json, 图片生成/文生图/klein_文生图+图像编辑【雄舟天文馆版】_2047099039581216770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_52

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen3.5+Klein AI 短剧漫剧｜自动写剧情一键出九宫格分镜_2046582075771326466.json、图片生成/图生图/klein双图_2017158118563647490.json、图片生成/文生图/klein_文生图+图像编辑_2042538360702509058.json、图片生成/文生图/klein_文生图+图像编辑【雄舟天文馆版】_2047099039581216770.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelPatchTorchSettings` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `easy promptLine` —— 2/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `InversionDemoLazySwitch` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `Seed Everywhere` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Text` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
