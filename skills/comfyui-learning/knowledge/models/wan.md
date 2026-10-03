---
name: wan
title: Wan 视频生成模型（Wan2.1 / Wan2.2）
category: models
tags: [wan, video, i2v, t2v, hunyuan-latent, lora]
updated: 2026-10-04
---

# Wan 视频生成模型（Wan2.1 / Wan2.2，阿里通义万相）

## 作用
开源视频生成模型族，ComfyUI 生态支持完善的视频扩散模型。本项目做视频生成（MiniMax H3），
Wan 是最常对照参考的开源视频链路，其节点习惯（视频 latent、帧数/帧率约定）在
H3 类视频工作流中大量复用。

## 版本矩阵

| 版本 | 任务 | 特点 |
|---|---|---|
| Wan2.1 T2V 1.3B/14B | 文生视频 | 1.3B 轻量，14B 质量 |
| Wan2.1 I2V 14B | 图生视频 | 首/尾帧控制 |
| Wan2.2 T2V/I2V A14B | 文/图生视频 | **双模型分高低噪**（MoE 思路） |
| Wan2.2 TI2V 5B | 图生视频 | 单模型 720p，24fps |
| Wan2.2 Fun / S2V /-animate | 控制版 | V2V、骨骼、口型等控制 |

## 2.2 双模型两段采样（重要机制）
Wan2.2 A14B 分 `high noise` 与 `low noise` 两个 diffusion_model：
- 前半程（约 0–50%）用 **high noise** 模型打构图与运动，
- 后半程用 **low noise** 模型收细节。
- ComfyUI 里常见两段 `KSampler`（或 SamplerCustomAdvanced + 两个 UNET 加载器）串联，
  由 `WanImageToVideo` / `WanFunControlToVideo` 等条件节点统一供 LATENT 与 conditioning。
- 新版 ComfyUI 支持在单个采样节点内双模型调度（`split_sigmoid` 类配置），二选一即可。

## 四件套组件
```
UNETLoader / Load Model        → wan2.2_*.safetensors（fp8 常见）
CLIPLoader(type=wan)           → umt5_xxl_fp8_e4m3fn_scaled.safetensors
CLIPVisionLoader               → clip_vision_h.safetensors（I2V 用）
VAELoader                      → wan_2.1_vae.safetensors（2.1/2.2 通用）
```

## 关键参数（视频链路必查）

| 参数 | 惯例 |
|---|---|
| 长度 length（帧数） | 81 帧 ≈ 5 秒 @16fps；必须 4n+1（Wan2.1），2.2 TI2V 为 121 帧@24fps |
| fps | 16（2.1 系）/ 24（2.2 TI2V），导出由 VideoCombine 决定 |
| 分辨率 | 832×480、480×832（A14B 常用）；TI2V 1280×704 |
| cfg | T2V/I2V 5–6；Fun 蒸馏版 1.0 |
| steps | 常规 20–30；配蒸馏 LoRA 4–8 步 |
| scheduler | `simple` 或 `beta`，shift 5–8（高分辨率调高） |

## 加速 LoRA
- `Wan2.1-LightX2V`（14B 4步/8步）、`Wan22-LightX2V` 蒸馏 LoRA：
  steps 降到 4–8、cfg=1、scheduler= simple/beta，速度数量级提升，动态略降。
- `CausVid` 等因果蒸馏 LoRA 同理。LoRA 强度 0.8–1.0。

## 使用要点
- I2V 首帧图分辨率要与 latent 尺寸一致，`WanImageToVideo` 会按图裁剪。
- 视频显存压力大：fp8 权重 + `empty latent`（视频版）+ tiled VAE 是三板斧；
  项目内 MultiGPU/FastLoad 节点（见 NODES_SOURCES.md）可分卡加载 high/low 两个模型。
- 输出统一走 `VHS_VideoCombine`（VideoHelperSuite）或 SaveWEBM/SaveAnimatedMP4。

## 常见坑
- 帧数不满足 4n+1 报错或时长错乱。
- 16fps 素材配 24fps 导出 → 动作变快，fps 要全程统一。
- high/low 模型接反 → 前段细节化后段糊化，画面崩坏。
- cfg>1 配蒸馏 LoRA → 过曝烧帧。

## 关联卡片
- `nodes/sampler.md`（两段采样实现）
- `concepts/latent.md`（视频 latent 时间维）
- `models/flux.md`（同为 DiT 系加载方式）
- TODO(待验证)：本项目 MiniMax H3 专属节点链路与 Wan 的差异对照卡，待首个 H3 工作流分析后沉淀。
