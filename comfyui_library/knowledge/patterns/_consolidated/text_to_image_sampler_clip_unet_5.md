---
name: text_to_image_sampler_clip_unet_5
type: Text To Image
frequency: 32
level: weak
coverage: 0.898656
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, TTResolutionSelector, UNETLoader, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/krea2+Qwen3.5-自动多风格文生图_2084922609443102721.json, 图片生成/文生图/Krea 2田园风格感文生图处理工作流_2101011311219003393.json, 图片生成/文生图/Krea2全自动反推工作流 文生图提示词反推_2100275220467773441.json, 图片生成/文生图/krea2 MJ风格工作流 美学风格生成_2109041547172999169.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2072869610650689537.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084176385911902210.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084180097455710209.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084184981282312193.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084188539746611201.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084191590809165826.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084543653397221377.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084547006332231681.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084566111013662721.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084568266718142466.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2086317060350631938.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2086324082525696001.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2089597886714699778.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2089606694295924738.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2093221605420916737.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2093225496157970434.json, 图片生成/文生图/krea2_MJ风格工作流_2108594095500386306.json, 图片生成/文生图/krea2全自动反推工作流_2099842463920902146.json, 图片生成/文生图/krea2田园风格MJ感工作流_2100583054992568322.json, 图片生成/文生图/krea2田园风格MJ感工作流_2102923019374125057.json, 图片生成/文生图/krea2田园风格MJ感工作流_2104384123690373122.json, 图片生成/文生图/krea2田园风格MJ感工作流_2104754840189624322.json, 图片生成/文生图/krea2田园风格MJ感工作流｜文生图氛围感拉满_2100772461267734530.json, 图片生成/文生图/全自动krea2万物迁移_万物复刻_2070712730314694658.json, 图片生成/文生图/多风格文生图｜krea2+Qwen3.5自动生成_2089836661319487489.json, 图片生成/文生图/多风格自动文生图｜Qwen3.5+krea2风格轮换生成_2093467909044658177.json, 图片生成/文生图/自动多风格文生图｜krea2+Qwen3.5一键直出_2093466592263888897.json, 视频生成/图生视频/krea2+Qwen3.5-自动多风格文生图 (1)_2085254333008007169.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（图片生成/图生图/krea2+Qwen3.5-自动多风格文生图_2084922609443102721.json、图片生成/文生图/Krea 2田园风格感文生图处理工作流_2101011311219003393.json、图片生成/文生图/Krea2全自动反推工作流 文生图提示词反推_2100275220467773441.json、图片生成/文生图/krea2 MJ风格工作流 美学风格生成_2109041547172999169.json、图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2072869610650689537.json…）

- **类型**：Text To Image
- **样本数**：32
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 32 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 31/32 个有
- `VAEDecode` —— 31/32 个有
- `LoraLoaderModelOnly` —— 30/32 个有
- `Label (rgthree)` —— 23/32 个有
- `ShowText|pysssss` —— 21/32 个有
- `ConditioningKrea2Rebalance` —— 10/32 个有
- `SetNode` —— 10/32 个有
- `孤海注释` —— 8/32 个有
- `JjkText` —— 7/32 个有
- `solarL_SaveImagesToZip` —— 7/32 个有
- `LoadImage` —— 4/32 个有
- `MuyeLoadImage` —— 2/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 1024 | 32 | 42% |
| 高度 | 512 | 80 - 1024 | 32 | 42% |
| 采样步数 | 8 | 4 - 8 | 32 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 32 | 18% |
| 采样算法 | euler | - | 32 | 78% |
| 调度器 | simple | - | 32 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 32 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 39/32 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/32 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 1024，32 个样本，取值分散，一致性仅 42%
- 高度 中位数 512，观测区间 80 - 1024，32 个样本，取值分散，一致性仅 42%
- 采样步数 中位数 8，观测区间 4 - 8，32 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，32 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，32 个样本，一致性 78%
- 调度器 最常用 simple，32 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，32 个样本，取值集中（一致性 100%）
- 高发问题（39/32 个样本）：Steps较低可能导致细节不足
