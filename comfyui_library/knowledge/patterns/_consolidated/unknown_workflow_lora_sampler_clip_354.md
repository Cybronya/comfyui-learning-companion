---
name: unknown_workflow_lora_sampler_clip_354
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DetailDaemonSamplerNode, EmptySD3LatentImage, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, StringConstantMultiline, TripleCLIPLoader, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【老金驿站】FluxSigma人物极致细节_1891710421731069953.json, 平台全量/【老金驿站】FLUXSigma人物极致细节+32K极致放大_1892132384844980225.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_354

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【老金驿站】FluxSigma人物极致细节_1891710421731069953.json、平台全量/【老金驿站】FLUXSigma人物极致细节+32K极致放大_1892132384844980225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DetailDaemonSamplerNode`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringConstantMultiline`
- `TripleCLIPLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `MultiplySigmas` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `TripleCLIPLoaderGGUF` —— 1/2 个有
- `UltimateSDUpscaleCustomSample` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
