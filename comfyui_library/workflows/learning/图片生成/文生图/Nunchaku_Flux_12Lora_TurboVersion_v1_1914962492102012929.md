---
key: 图片生成/文生图/Nunchaku_Flux_12Lora_TurboVersion_v1_1914962492102012929.json
name: Nunchaku_Flux_12Lora_TurboVersion_v1_1914962492102012929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku_Flux_12Lora_TurboVersion_v1_1914962492102012929.json
hash: 9ce8d9427779922d
coverage: 1
learned_at: 2026-10-10 20:58:48
nodes: [SamplerCustomAdvanced, SamplerCustomAdvanced, SamplerCustomAdvanced, VAEDecode, VAEDecode, VAEDecode, BasicGuider, BasicGuider, BasicGuider, BasicGuider, VAEDecode, BasicGuider, SamplerCustomAdvanced, SamplerCustomAdvanced, SamplerCustomAdvanced, VAEDecode, VAEDecode, VAEDecode, BasicGuider, BasicGuider, BasicGuider, SamplerCustomAdvanced, SamplerCustomAdvanced, VAEDecode, BasicGuider, SamplerCustomAdvanced, SamplerCustomAdvanced, VAEDecode, VAEDecode, VAEDecode, BasicGuider, BasicGuider, BasicGuider, SamplerCustomAdvanced, KSamplerSelect, KSamplerSelect, BasicScheduler, KSamplerSelect, BasicScheduler, KSamplerSelect, BasicScheduler, KSamplerSelect, KSamplerSelect, BasicScheduler, BasicScheduler, VAEDecode, SaveImage, SaveImage, SaveImage, SamplerCustomAdvanced, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, NunchakuFluxLoraLoader, BasicScheduler, BasicScheduler, BasicScheduler, BasicScheduler, BasicScheduler, BasicScheduler, BasicScheduler, SaveImage, EmptyLatentImage, NunchakuFluxLoraLoader, SaveImage, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, VAELoader, DualCLIPLoader, NunchakuFluxDiTLoader, KSamplerSelect, CLIPTextEncodeFlux, RandomNoise]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1280, "width": 720}
---

# 图片生成/文生图/Nunchaku_Flux_12Lora_TurboVersion_v1_1914962492102012929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku_Flux_12Lora_TurboVersion_v1_1914962492102012929.json`

## 结构

**节点**（85 个）：
- `SamplerCustomAdvanced`
- `SamplerCustomAdvanced`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `BasicGuider`
- `BasicGuider`
- `BasicGuider`
- `BasicGuider`
- `VAEDecode`
- `BasicGuider`
- `SamplerCustomAdvanced`
- `SamplerCustomAdvanced`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `BasicGuider`
- `BasicGuider`
- `BasicGuider`
- `SamplerCustomAdvanced`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `BasicGuider`
- `SamplerCustomAdvanced`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `BasicGuider`
- `BasicGuider`
- `BasicGuider`
- `SamplerCustomAdvanced`
- `KSamplerSelect`
- `KSamplerSelect`
- `BasicScheduler`
- `KSamplerSelect`
- `BasicScheduler`
- `KSamplerSelect`
- `BasicScheduler`
- `KSamplerSelect`
- `KSamplerSelect`
- `BasicScheduler`
- `BasicScheduler`
- `VAEDecode`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `NunchakuFluxLoraLoader`
- `BasicScheduler`
- `BasicScheduler`
- `BasicScheduler`
- `BasicScheduler`
- `BasicScheduler`
- `BasicScheduler`
- `BasicScheduler`
- `SaveImage`
- `EmptyLatentImage`
- `NunchakuFluxLoraLoader`
- `SaveImage`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `VAELoader`
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `KSamplerSelect`
- `CLIPTextEncodeFlux`
- `RandomNoise`

## 关键参数

- `batch_size` = `1`
- `height` = `1280`
- `width` = `720`

## 知识

覆盖率 **100%**（85/85）

**有卡**：`SamplerCustomAdvanced`、`VAEDecode`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`SaveImage`、`NunchakuFluxLoraLoader`、`EmptyLatentImage`、`VAELoader`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`CLIPTextEncodeFlux`、`RandomNoise`
