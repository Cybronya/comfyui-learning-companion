---
name: unknown_workflow_controlnet_upscale_lora_6
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.835333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetLoader, DWPreprocessor, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, LoraLoader, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StringFunction|pysssss, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX IP角色 三视图多角度 CN控制_1931916122629537793.json, 平台全量/【人物一致多角度】FLUX完美三视图IP角色创建_1915585562839810049.json, 平台全量/【完美真实】FLUX IP角色 三视图多角度 CN控制+后期高清放大_1929333943978594305.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX IP角色 三视图多角度 CN控制_1931916122629537793.json、平台全量/【人物一致多角度】FLUX完美三视图IP角色创建_1915585562839810049.json、平台全量/【完美真实】FLUX IP角色 三视图多角度 CN控制+后期高清放大_1929333943978594305.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetLoader`
- `DWPreprocessor`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `Simple String` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | 0.75 - 0.75 | 3 | 100% |
| LoRA 模型强度 | 0.9 | 0.7 - 0.9 | 3 | 89% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.75，观测区间 0.75 - 0.75，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.9，观测区间 0.7 - 0.9，3 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
