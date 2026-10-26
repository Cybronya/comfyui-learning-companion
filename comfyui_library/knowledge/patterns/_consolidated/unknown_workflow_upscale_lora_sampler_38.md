---
name: unknown_workflow_upscale_lora_sampler_38
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.991667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, FlowMatchEulerDiscreteScheduler (Custom), KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-Turbo文生图_2003476119510786049.json, 图片生成/文生图/凌波_2104236095805419521.json, 图片生成/文生图/含章plus pro max v7_2094807352477315073.json, 图片生成/文生图/含章plus pro max决定版_2101643981267488770.json, 图片生成/文生图/鱼龙百变_2106036449396215809.json, 图片生成/文生图/鱼龙百变_2114525151864901634.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-image-Turbo文生图_2003476119510786049.json、图片生成/文生图/凌波_2104236095805419521.json、图片生成/文生图/含章plus pro max v7_2094807352477315073.json、图片生成/文生图/含章plus pro max决定版_2101643981267488770.json、图片生成/文生图/鱼龙百变_2106036449396215809.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/6 个有
- `CR Prompt Text` —— 5/6 个有
- `EmptySD3LatentImage` —— 5/6 个有
- `LayerColor: BrightnessContrastV2` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `TextConcat` —— 5/6 个有
- `CFGGuider` —— 1/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
