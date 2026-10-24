---
name: image_to_image_lora_sampler_unet_70
type: Image To Image
frequency: 9
level: strong
coverage: 0.917556
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2096490894571687937.json, 图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097045177390166018.json, 图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097051371597033473.json, 图片生成/图生图/动漫头像 漫画头像  真人转动漫  真人转卡通  真人转漫画_2095747766894022658.json, 图片生成/图生图/千问2511_任意物体360°视角随心切换_手动滑块操作更便捷_2010697372224987138.json, 图片生成/图生图/千问Qwen Edit 2511任意切换视觉_2010756226547716098.json, 图片生成/图生图/双图编辑-图片人物替换-AIGC大赏-修改_2090115164480827393.json, 图片生成/图生图/双图编辑-图片人物替换-AIGC大赏_2043255864382988289.json, 图片生成/图生图/提示词替换人物_2111667142767763458.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_70

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2096490894571687937.json、图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097045177390166018.json、图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097051371597033473.json、图片生成/图生图/动漫头像 漫画头像  真人转动漫  真人转卡通  真人转漫画_2095747766894022658.json、图片生成/图生图/千问2511_任意物体360°视角随心切换_手动滑块操作更便捷_2010697372224987138.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 7/9 个有
- `PreviewImage` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `PIP_图像联结` —— 5/9 个有
- `SeedVR2LoadDiTModel` —— 5/9 个有
- `SeedVR2LoadVAEModel` —— 5/9 个有
- `SeedVR2VideoUpscaler` —— 5/9 个有
- `TextEncodeQwenImageEditPlus` —— 5/9 个有
- `CR Text` —— 4/9 个有
- `TextEncodeQwenImageEdit` —— 4/9 个有
- `CompressImages` —— 3/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/9 个有
- `ImageConcanate` —— 3/9 个有
- `QwenMultiangleCameraNode` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `ImpactSwitch` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `Text` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
