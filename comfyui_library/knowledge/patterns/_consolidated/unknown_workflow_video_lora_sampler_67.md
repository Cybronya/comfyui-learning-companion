---
name: unknown_workflow_video_lora_sampler_67
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.997056
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, LoraLoader, TeaCache, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/专业级电影运镜 Motion｜一键生成视频系列_1907317036790505474.json, 视频生成/图生视频/360度盲盒旋转展示工作流 WAN2.1 ｜一键生成视频系列_1907272567051444225.json, 视频生成/图生视频/NFT卡牌 360度旋转展示工作流 WAN2.1｜一键生成视频系列_1914851220903686145.json, 视频生成/图生视频/WAN 2.1 和年轻的自己自拍 一键生成视频系列_1908884994994151426.json, 视频生成/图生视频/WAN2.1图生视频360度旋转_1906686265050247170.json, 视频生成/图生视频/WAN2.1图生视频一键变身恶灵骑士_1912469568701329410.json, 视频生成/图生视频/WAN2.1图生视频万物成盒_1913534894562078722.json, 视频生成/图生视频/WAN2.1图生视频美女原地起飞_1908140275909468162.json, 视频生成/图生视频/WAN2.1图生视频美女射击_1910308143438491650.json, 视频生成/图生视频/WAN2.1图生视频美女转身_1909579567680684034.json, 视频生成/图生视频/WAN2.1美女热舞大摆锤_1908472121150812161.json, 视频生成/图生视频/Wan2.1 人物小丑面具特效｜i2V_1911952901085036546.json, 视频生成/图生视频/Wan2.1 愤怒人物表情特效｜i2V_1911801404531638273.json, 视频生成/图生视频/Wan2.1_人物哭泣特效｜i2V_1912077836331511810.json, 视频生成/图生视频/【360度旋转】wan2.1人物生成+万物旋转动画视频展示_1911646094139555841.json, 视频生成/图生视频/【七龙珠元气弹特效】wan2.1人物发射元气弹特效_1911792144137318401.json, 视频生成/图生视频/任意物体360度旋转展示 ｜盲盒、泡泡玛特_1910201244638740482.json, 视频生成/图生视频/抖胸舞跳起来_1921368068402921474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/专业级电影运镜 Motion｜一键生成视频系列_1907317036790505474.json、视频生成/图生视频/360度盲盒旋转展示工作流 WAN2.1 ｜一键生成视频系列_1907272567051444225.json、视频生成/图生视频/NFT卡牌 360度旋转展示工作流 WAN2.1｜一键生成视频系列_1914851220903686145.json、视频生成/图生视频/WAN 2.1 和年轻的自己自拍 一键生成视频系列_1908884994994151426.json、视频生成/图生视频/WAN2.1图生视频360度旋转_1906686265050247170.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `TeaCache`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 11/18 个有
- `UnetLoaderGGUF` —— 11/18 个有
- `ConcatTextOfUtils` —— 10/18 个有
- `Joy_caption` —— 10/18 个有
- `Joy_caption_load` —— 10/18 个有
- `UNETLoader` —— 7/18 个有
- `Int` —— 1/18 个有
- `JjkText` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 18 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 18 | 100% |
| 采样算法 | uni_pc | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 18 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 18/18 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：发现KSampler但没有VAEDecode
