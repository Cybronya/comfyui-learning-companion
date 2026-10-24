---
name: unknown_workflow_sampler_clip_unet_78
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.898455
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_chroma_text_to_image.json, 图片生成/文生图/Chroma-V35前瞻文生图测试_1931586622008000513.json, 图片生成/文生图/Chroma1-HD 文生图_1962355322230915073.json, 图片生成/文生图/F.2-klein-9B+LoRA文生图工作流_2013075554722914305.json, 图片生成/文生图/FLUX klein 4B 文生图_2013180405410697218.json, 图片生成/文生图/FLUX klein 9B 文生图_2013484429548724225.json, 图片生成/文生图/FLUX2-KLEIN+lora+快速生图_2012490189339365377.json, 图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012040141979783169.json, 图片生成/文生图/Flux.2 [Klein]：文生图4B ComfyUI官方流_2012049122789953538.json, 图片生成/文生图/Flux2-klein-base-9b-fp8 文生图_2013133653185929218.json, 图片生成/文生图/Flux2.Klein基础文生图工作流_2014585003874717698.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_78

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（comfyui-workflow-templates-json/image_chroma_text_to_image.json、图片生成/文生图/Chroma-V35前瞻文生图测试_1931586622008000513.json、图片生成/文生图/Chroma1-HD 文生图_1962355322230915073.json、图片生成/文生图/F.2-klein-9B+LoRA文生图工作流_2013075554722914305.json、图片生成/文生图/FLUX klein 4B 文生图_2013180405410697218.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 8/11 个有
- `Flux2Scheduler` —— 8/11 个有
- `PrimitiveInt` —— 7/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `BasicScheduler` —— 3/11 个有
- `EmptySD3LatentImage` —— 3/11 个有
- `T5TokenizerOptions` —— 3/11 个有
- `LoraLoader` —— 2/11 个有
- `ModelSamplingAuraFlow` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy promptList` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1.5 | - | 2 | 100% |
| LoRA 文本强度 | 1.41 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1.41，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
