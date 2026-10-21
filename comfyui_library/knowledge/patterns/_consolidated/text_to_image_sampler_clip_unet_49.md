---
name: text_to_image_sampler_clip_unet_49
type: Text To Image
frequency: 9
level: weak
coverage: 0.903778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima -aesthetic-v1.1-自动优化提示词-动漫文生图_2078551646241648642.json, 图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json, 图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json, 图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json, 图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json, 图片生成/文生图/Krea2-双图风格融合-T8版_2070051493448867842.json, 图片生成/文生图/Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322.json, 图片生成/文生图/Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682.json, 图片生成/文生图/文生图参考生图二合一改进版｜双模式图像生成工作流_2108383787649425409.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_49

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Anima -aesthetic-v1.1-自动优化提示词-动漫文生图_2078551646241648642.json、图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json、图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json、图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json、图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/9 个有
- `ShowText|pysssss` —— 5/9 个有
- `ResolutionSelector` —— 4/9 个有
- `llama_cpp_instruct_adv` —— 4/9 个有
- `llama_cpp_model_loader` —— 4/9 个有
- `ConditioningZeroOut` —— 3/9 个有
- `LoadImage` —— 3/9 个有
- `QwenImage21Cache` —— 3/9 个有
- `TextGenerateLTX2Prompt` —— 3/9 个有
- `JjkText` —— 2/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `solarL_SaveImagesToZip` —— 2/9 个有
- `孤海注释` —— 2/9 个有
- `AnimaLLLiteApply` —— 1/9 个有
- `BatchImagesNode` —— 1/9 个有
- `RHLLMChatNode` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `SaveImageAdvanced` —— 1/9 个有
- `TextEncodeQwenImage21` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 40 | 9 | 41% |
| Prompt 约束强度(CFG) | 4 | 1 - 4.5 | 9 | 61% |
| 采样算法 | er_sde | - | 9 | 56% |
| 调度器 | simple | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 80 - 1080 | 9 | 50% |
| 高度 | 1024 | 80 - 1920 | 9 | 43% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 40，9 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4.5，9 个样本
- 采样算法 最常用 er_sde，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1080，9 个样本
- 高度 中位数 1024，观测区间 80 - 1920，9 个样本，取值分散，一致性仅 43%
