---
name: text_to_image_lora_sampler_clip_45
type: Text To Image
frequency: 18
level: weak
coverage: 0.926778
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2 手机随地大小拍_2086001026607439874.json, 图片生成/文生图/krea2 质感和清晰度增强唯美人像写真_2073682470511398914.json, 图片生成/文生图/seedvr2 4K直出人像精修写真 含章文生图特化lora_2094242378528935938.json, 图片生成/文生图/偏raw写真风格v2文生图｜虚实之间人像写真工作流_2087229110069317634.json, 图片生成/文生图/偏精修写真风格v5文生图｜虚实之间人像写真工作流_2087227931155329026.json, 图片生成/文生图/写实美少女文生图｜含章人像写真图片生成工作流_2088150755827081218.json, 图片生成/文生图/写真风格偏raw质感lora｜虚实之间v2单反模拟文生图_2088757626908798978.json, 图片生成/文生图/写真风格偏精修lora｜虚实之间v5单反模拟文生图人像_2088756228964052994.json, 图片生成/文生图/含章+seedvr2组合｜4K直出文生图高清生成_2094359568724881409.json, 图片生成/文生图/含章plus pro max v7｜美少女人像写真文生图_2096322594084581377.json, 图片生成/文生图/含章plus pro max决定版｜zimage人像精修写真特化｜对齐更稳定_2101880290653331458.json, 图片生成/文生图/含章人像精修写真lora 文生图美少女写实特化_2094243785067810818.json, 图片生成/文生图/含章人像精修写真lora｜文生图美少女写实特化_2089039018632761345.json, 图片生成/文生图/含章文生图工作流｜美少女写实风一键高清生成_2094590893402705921.json, 图片生成/文生图/鱼龙百变人像写真文生图｜写实风格随机变换百变造型_2108033206091075586.json, 图片生成/文生图/鱼龙百变写实人像写真，文生图风格随心切换_2110792049208414209.json, 图片生成/文生图/鱼龙百变工作流，人像写真文生图写实风格处理工具_2108443506875392002.json, 图片生成/文生图/鱼龙百变｜人像写真文生图一键直出写实质感大片_2110675701501353985.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/krea2 手机随地大小拍_2086001026607439874.json、图片生成/文生图/krea2 质感和清晰度增强唯美人像写真_2073682470511398914.json、图片生成/文生图/seedvr2 4K直出人像精修写真 含章文生图特化lora_2094242378528935938.json、图片生成/文生图/偏raw写真风格v2文生图｜虚实之间人像写真工作流_2087229110069317634.json、图片生成/文生图/偏精修写真风格v5文生图｜虚实之间人像写真工作流_2087227931155329026.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 16/18 个有
- `JjkText` —— 16/18 个有
- `LayerColor: BrightnessContrastV2` —— 16/18 个有
- `solarL_SaveImagesToZip` —— 16/18 个有
- `孤海注释` —— 16/18 个有
- `CR Prompt Text` —— 14/18 个有
- `SeedVR2LoadDiTModel` —— 14/18 个有
- `SeedVR2LoadVAEModel` —— 14/18 个有
- `SeedVR2VideoUpscaler` —— 14/18 个有
- `TextConcat` —— 14/18 个有
- `CLIPLoaderGGUF` —— 10/18 个有
- `BasicGuider` —— 6/18 个有
- `FlowMatchEulerDiscreteScheduler (Custom)` —— 6/18 个有
- `KSamplerSelect` —— 6/18 个有
- `RandomNoise` —— 6/18 个有
- `SamplerCustomAdvanced` —— 6/18 个有
- `KSamplerAdvanced` —— 4/18 个有
- `ModelSamplingAuraFlow` —— 4/18 个有
- `ComfySwitchNode` —— 2/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1368 | 18 | 0% |
| 高度 | 80 | 80 - 2048 | 18 | 0% |
| 采样步数 | 4 | 4 - 8 | 18 | 72% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 18 | 73% |
| 采样算法 | er_sde | - | 18 | 89% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1368，18 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 2048，18 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，18 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，18 个样本
- 采样算法 最常用 er_sde，18 个样本，一致性 89%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（24/18 个样本）：Steps较低可能导致细节不足
