---
name: text_to_image_sampler_clip_unet_9
type: Text To Image
frequency: 26
level: moderate
coverage: 0.931346
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json, 图片生成/文生图/YJ-APP-Zimage-文生图-瑶光_2038252771387908097.json, 图片生成/文生图/Z-image-base文生图_2016192732154306562.json, 图片生成/文生图/Z-image-base文生图官方版_2018889742305202178.json, 图片生成/文生图/Z-image-turbo文生图3D国漫CG风格_2074209841383567362.json, 图片生成/文生图/Z-image-turbo文生图赛璐璐平涂动漫风格_2077821791761948673.json, 图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_2076587497584414722.json, 图片生成/文生图/qwen2512文生图泳装系列_2041408599649423361.json, 图片生成/文生图/qwen_edit_2512_越真实文生图-真实去ai味_2010517531177521153.json, 图片生成/文生图/古风美女Qwen2512文生图真实人像质感御姐美女_2042569664789745666.json, 图片生成/文生图/吊带睡衣Qwen2512文生图真实人像质感御姐美女_2041454987309486082.json, 图片生成/文生图/吊带睡衣Qwen2512文生图真实人像质感御姐美女_2041490961523544065.json, 图片生成/文生图/城市夜景Qwen2512文生图真实人像质感御姐美女_2042547778978586625.json, 图片生成/文生图/外国比基尼Qwen2512真实人像质感御姐美女_2041444022757101569.json, 图片生成/文生图/外国泳衣Qwen2512文生图真实人像质感御姐美女_2041446359529689090.json, 图片生成/文生图/婚纱美女Qwen2512文生图真实人像质感御姐美女_2042552387361050625.json, 图片生成/文生图/学生妹Qwen2512文生图真实人像质感御姐美女_2042566625039224833.json, 图片生成/文生图/居家美女Qwen2512文生图真实人像质感御姐美女_2042601654381449218.json, 图片生成/文生图/巷子印花Qwen2512文生图真实人像质感御姐美女_2042604243156209665.json, 图片生成/文生图/异域风情Qwen2512文生图真实人像质感御姐美女_2042469704727531521.json, 图片生成/文生图/性感女讲师Qwen2512文生图真实人像质感御姐美女_2042584095405907969.json, 图片生成/文生图/性感有韵味Qwen2512文生图真实人像质感御姐美女_2042577587704172546.json, 图片生成/文生图/成熟有气质Qwen2512文生图真实人像质感御姐美女_2041496999802966017.json, 图片生成/文生图/文字头像抽卡神器_自动生成_2084090261851955202.json, 图片生成/文生图/风格文字头像自动生成_2080232577151102978.json, 图片生成/文生图/🦁国产之光 Qwen-image2512震撼来袭【随机提示词】_2007665464629010433.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json、图片生成/文生图/YJ-APP-Zimage-文生图-瑶光_2038252771387908097.json、图片生成/文生图/Z-image-base文生图_2016192732154306562.json、图片生成/文生图/Z-image-base文生图官方版_2018889742305202178.json、图片生成/文生图/Z-image-turbo文生图3D国漫CG风格_2074209841383567362.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 23/26 个有
- `CR Text` —— 22/26 个有
- `ModelSamplingAuraFlow` —— 9/26 个有
- `RH_LLMAPI_NODE` —— 4/26 个有
- `CR Latent Input Switch` —— 3/26 个有
- `DapaoImageRatioLimitNode` —— 3/26 个有
- `Seed (rgthree)` —— 3/26 个有
- `easy cleanGpuUsed` —— 3/26 个有
- `easy int` —— 3/26 个有
- `PrimitiveInt` —— 2/26 个有
- `InversionDemoLazyIndexSwitch` —— 1/26 个有
- `Note Plus (mtb)` —— 1/26 个有
- `QwenEditResolution` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 50 | 26 | 51% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 26 | 56% |
| 采样算法 | euler_ancestral | - | 26 | 58% |
| 调度器 | simple | - | 26 | 81% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |
| 宽度 | 768 | 16 - 1536 | 26 | 67% |
| 高度 | 1344 | 16 - 2080 | 26 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 50，26 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，26 个样本
- 采样算法 最常用 euler_ancestral，26 个样本，一致性 58%
- 调度器 最常用 simple，26 个样本，一致性 81%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 16 - 1536，26 个样本
- 高度 中位数 1344，观测区间 16 - 2080，26 个样本
