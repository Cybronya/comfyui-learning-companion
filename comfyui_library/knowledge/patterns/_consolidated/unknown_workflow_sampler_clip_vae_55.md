---
name: unknown_workflow_sampler_clip_vae_55
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8885
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, FluxGuidance, KSamplerSelect, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux秒级极速nunchaku版_1913094526456557570.json, 图片生成/文生图/OmniConsistency  文生图_1927931879364935681.json, 图片生成/文生图/【AI由北】nunchaku-flux.1_1915753087057723394.json, 图片生成/文生图/双截棍Pulid换脸秒出图_1924625965945974786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_55

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux秒级极速nunchaku版_1913094526456557570.json、图片生成/文生图/OmniConsistency  文生图_1927931879364935681.json、图片生成/文生图/【AI由北】nunchaku-flux.1_1915753087057723394.json、图片生成/文生图/双截棍Pulid换脸秒出图_1924625965945974786.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `NunchakuFluxLoraLoader` —— 3/4 个有
- `Text Multiline` —— 2/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `NunchakuPulidApply` —— 1/4 个有
- `NunchakuPulidLoader` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
